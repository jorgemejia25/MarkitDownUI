# MarkItDown UI

[![Python](https://img.shields.io/badge/Python-3.10+-blue.svg)](https://python.org)
[![Flask](https://img.shields.io/badge/Flask-3.0.0-green.svg)](https://flask.palletsprojects.com/)
[![MarkItDown](https://img.shields.io/badge/MarkItDown-0.1.3-orange.svg)](https://github.com/microsoft/markitdown)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

A modern web application for converting various document formats to Markdown using Microsoft's MarkItDown library. Features a clean, minimalist interface for converting PDF, Word, PowerPoint, Excel, and other document formats to Markdown with drag-and-drop functionality.

## Features

- **Multi-format Support**: Convert PDF, Word (.docx, .doc), PowerPoint (.pptx, .ppt), Excel (.xlsx, .xls), HTML, CSV, JSON, XML, and EPUB files
- **Clean UI**: Minimalist design without shadows or emojis, following clean UI principles
- **Drag & Drop**: Intuitive file upload with drag and drop functionality
- **Real-time Conversion**: Convert documents to Markdown instantly
- **Download & Copy**: Download converted files or copy content to clipboard
- **macOS App**: Native macOS application for easy launching
- **Automatic Dependencies**: Self-installing dependencies and browser integration

## Quick Start

### Option 1: Direct Python Execution
```bash
git clone https://github.com/jorgemejia25/MarkitDownUI.git
cd MarkitDownUI
pip install -r requirements.txt
python3 app.py
```

### Option 2: macOS Native App
```bash
git clone https://github.com/jorgemejia25/MarkitDownUI.git
cd MarkitDownUI
./create_app.sh
# Double-click MarkItDown.app on your Desktop
```

## Installation

### Prerequisites

- Python 3.10 or higher
- macOS (for the native app)

### Quick Start

1. **Clone the repository**
   ```bash
   git clone https://github.com/jorgemejia25/MarkitDownUI.git
   cd MarkitDownUI
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the application**
   ```bash
   python3 app.py
   ```

4. **Open in browser**
   Navigate to `http://localhost:5001`

### macOS Native Application

For the easiest experience on macOS:

1. **Create the native app**
   ```bash
   ./create_app.sh
   ```

2. **Use the app**
   - Double-click `MarkItDown.app` on your Desktop
   - The browser will open automatically
   - Press Enter in the terminal to close

## Usage

### Web Interface

1. **Upload a file**
   - Drag and drop a file onto the upload area
   - Or click "Seleccionar Archivo" to choose a file

2. **Convert to Markdown**
   - Click "Convertir a Markdown"
   - Wait for the conversion to complete

3. **Get the result**
   - View the Markdown content in the preview area
   - Click "Copiar" to copy to clipboard
   - Click "Descargar" to download the .md file

### Supported Formats

| Format | Extensions | Description |
|--------|------------|-------------|
| PDF | .pdf | Portable Document Format |
| Word | .docx, .doc | Microsoft Word documents |
| PowerPoint | .pptx, .ppt | Microsoft PowerPoint presentations |
| Excel | .xlsx, .xls | Microsoft Excel spreadsheets |
| Text | .txt | Plain text files |
| HTML | .html | Web pages |
| CSV | .csv | Comma-separated values |
| JSON | .json | JavaScript Object Notation |
| XML | .xml | Extensible Markup Language |
| EPUB | .epub | Electronic publication format |

## API Endpoints

### GET /
Returns the main application page.

### POST /convert
Converts an uploaded file to Markdown.

**Request**: Multipart form data with a file field
**Response**: JSON with conversion results

```json
{
  "success": true,
  "markdown_content": "# Converted content...",
  "filename": "document.md",
  "download_path": "/download/uuid_document.md"
}
```

### GET /download/<filename>
Downloads a converted Markdown file.

### GET /health
Health check endpoint returning server status.

## Project Structure

```
MarkItDown/
├── app.py                 # Main Flask application
├── launch_app.py          # Application launcher
├── requirements.txt       # Python dependencies
├── templates/
│   └── index.html        # Web interface
├── uploads/              # Temporary upload directory
├── outputs/              # Converted files directory
├── .gitignore           # Git ignore rules
└── README.md            # This file
```

## Configuration

### File Size Limit
Default limit is 16MB. To change:
```python
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # 16MB
```

### Server Port
Default port is 5001. To change:
```python
app.run(debug=True, host='0.0.0.0', port=5001)
```

## Dependencies

- **Flask**: Web framework
- **MarkItDown**: Microsoft's document conversion library
- **Werkzeug**: WSGI utilities
- **python-dotenv**: Environment variable management

## Development

### Running in Development Mode

```bash
python3 app.py
```

The application runs with debug mode enabled on `http://localhost:5001`.

### Code Documentation

All code is documented with comprehensive docstrings following Python conventions:

- Module-level documentation
- Class and method documentation
- Parameter and return value descriptions
- Usage examples where appropriate

## Screenshots

The application features a clean, minimalist interface with:
- Drag and drop file upload
- Real-time conversion feedback
- Markdown preview and download
- Professional design without emojis or shadows

## Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## Troubleshooting

### Common Issues

**Port already in use**
- The application uses port 5001 by default
- Close other applications using this port
- Or modify the port in `app.py`

**Dependencies not found**
- Run `pip install -r requirements.txt`
- Ensure Python 3.10+ is installed

**File conversion errors**
- Check that the file format is supported
- Ensure the file is not corrupted
- Try with a smaller file size

**Browser doesn't open automatically**
- Navigate manually to `http://localhost:5001`
- Check firewall settings

### Error Messages

The application provides clear error messages in Spanish:
- "No se ha seleccionado ningún archivo" - No file selected
- "Tipo de archivo no soportado" - Unsupported file type
- "Error al convertir el archivo" - File conversion error

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- [Microsoft](https://github.com/microsoft/markitdown) for the MarkItDown library
- [Flask](https://flask.palletsprojects.com/) team for the web framework
- [TailwindCSS](https://tailwindcss.com/) for the styling framework

## Version History

- **v1.0.0**: Initial release with core functionality
  - Multi-format document conversion
  - Clean web interface
  - macOS native application
  - Comprehensive documentation

## Support

If you encounter any issues or have questions, please:
1. Check the [troubleshooting section](#troubleshooting)
2. Search existing [issues](https://github.com/jorgemejia25/MarkitDownUI/issues)
3. Create a new issue with detailed information

---

**Made with ❤️ by [jorgemejia25](https://github.com/jorgemejia25)**