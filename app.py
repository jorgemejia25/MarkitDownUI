"""
MarkItDown Web Application

A Flask web application that converts various document formats to Markdown
using Microsoft's MarkItDown library. Supports PDF, Word, PowerPoint, Excel,
and other common document formats.

Author: jorgemejia25
Version: 1.0.0
"""

from flask import Flask, request, jsonify, render_template, send_file
from markitdown import MarkItDown
import os
import tempfile
import uuid
from werkzeug.utils import secure_filename

# Initialize Flask application
app = Flask(__name__)
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # 16MB max file size

# Configure upload and output directories
UPLOAD_FOLDER = 'uploads'
OUTPUT_FOLDER = 'outputs'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(OUTPUT_FOLDER, exist_ok=True)

# Initialize MarkItDown converter
md_converter = MarkItDown()

# Supported file extensions
ALLOWED_EXTENSIONS = {
    'pdf', 'docx', 'doc', 'pptx', 'ppt', 'xlsx', 'xls', 
    'txt', 'html', 'csv', 'json', 'xml', 'epub'
}


def allowed_file(filename):
    """
    Check if the uploaded file has an allowed extension.
    
    Args:
        filename (str): The name of the file to check
        
    Returns:
        bool: True if the file extension is allowed, False otherwise
    """
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/')
def index():
    """
    Render the main application page.
    
    Returns:
        str: Rendered HTML template for the main page
    """
    return render_template('index.html')


@app.route('/convert', methods=['POST'])
def convert_file():
    """
    Convert uploaded file to Markdown format.
    
    Expects a file in the request form data. Validates the file type,
    saves it temporarily, converts it using MarkItDown, and returns
    the Markdown content along with download information.
    
    Returns:
        JSON response with either:
        - success: True, markdown_content, filename, download_path
        - error: Error message with appropriate HTTP status code
    """
    if 'file' not in request.files:
        return jsonify({'error': 'No se ha seleccionado ningún archivo'}), 400
    
    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': 'No se ha seleccionado ningún archivo'}), 400
    
    if not allowed_file(file.filename):
        return jsonify({'error': 'Tipo de archivo no soportado'}), 400
    
    try:
        # Save file temporarily
        filename = secure_filename(file.filename)
        unique_filename = f"{uuid.uuid4()}_{filename}"
        file_path = os.path.join(UPLOAD_FOLDER, unique_filename)
        file.save(file_path)
        
        # Convert file to Markdown
        result = md_converter.convert(file_path)
        
        # Save result to file
        output_filename = f"{os.path.splitext(filename)[0]}.md"
        output_path = os.path.join(OUTPUT_FOLDER, f"{uuid.uuid4()}_{output_filename}")
        
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(result.text_content)
        
        # Clean up temporary file
        os.remove(file_path)
        
        return jsonify({
            'success': True,
            'markdown_content': result.text_content,
            'filename': output_filename,
            'download_path': f'/download/{os.path.basename(output_path)}'
        })
        
    except Exception as e:
        # Clean up temporary file in case of error
        if 'file_path' in locals() and os.path.exists(file_path):
            os.remove(file_path)
        
        return jsonify({'error': f'Error al convertir el archivo: {str(e)}'}), 500


@app.route('/download/<filename>')
def download_file(filename):
    """
    Download a converted Markdown file.
    
    Args:
        filename (str): The name of the file to download
        
    Returns:
        File download response or error message
    """
    file_path = os.path.join(OUTPUT_FOLDER, filename)
    if os.path.exists(file_path):
        return send_file(file_path, as_attachment=True, download_name=filename)
    else:
        return jsonify({'error': 'Archivo no encontrado'}), 404


@app.route('/health')
def health_check():
    """
    Health check endpoint to verify server status.
    
    Returns:
        JSON response with server status information
    """
    return jsonify({'status': 'OK', 'message': 'Servidor funcionando correctamente'})

if __name__ == '__main__':
    """
    Run the Flask application in development mode.
    
    Starts the server on all interfaces (0.0.0.0) on port 5001
    with debug mode enabled for development.
    """
    app.run(debug=True, host='0.0.0.0', port=5001)
