# MarkItDown - Technical Documentation

## Architecture Overview

MarkItDown is a Flask-based web application that provides document conversion services using Microsoft's MarkItDown library. The application follows a clean architecture pattern with separation of concerns.

### Core Components

1. **Flask Application (`app.py`)**
   - Main web server and API endpoints
   - File upload handling and validation
   - Document conversion orchestration
   - Response formatting and error handling

2. **Launcher (`launch_app.py`)**
   - Application lifecycle management
   - Dependency verification and installation
   - Server process management
   - Browser integration and cleanup

3. **Web Interface (`templates/index.html`)**
   - Clean, minimalist user interface
   - Drag and drop file upload
   - Real-time conversion feedback
   - Result display and download functionality

## API Reference

### Endpoints

#### GET /
**Purpose**: Serve the main application interface
**Response**: HTML page with the conversion interface
**Status Codes**: 200 (success)

#### POST /convert
**Purpose**: Convert uploaded file to Markdown
**Request Body**: Multipart form data with file field
**Response**: JSON object with conversion results

**Success Response**:
```json
{
  "success": true,
  "markdown_content": "string",
  "filename": "string",
  "download_path": "string"
}
```

**Error Response**:
```json
{
  "error": "string"
}
```

**Status Codes**:
- 200: Conversion successful
- 400: Bad request (no file, unsupported format)
- 500: Internal server error

#### GET /download/<filename>
**Purpose**: Download converted Markdown file
**Parameters**: filename (string) - Name of the file to download
**Response**: File download or error message
**Status Codes**:
- 200: File download successful
- 404: File not found

#### GET /health
**Purpose**: Health check endpoint
**Response**: Server status information
**Status Codes**: 200 (always)

## Data Flow

### File Conversion Process

1. **File Upload**
   - Client uploads file via POST /convert
   - Server validates file type and size
   - File saved temporarily with unique identifier

2. **Conversion**
   - MarkItDown library processes the file
   - Content extracted and converted to Markdown
   - Result stored in memory and temporary file

3. **Response**
   - Markdown content returned to client
   - Download path provided for file access
   - Temporary files cleaned up

4. **Download**
   - Client requests file via GET /download/<filename>
   - Server streams file to client
   - File remains available for subsequent downloads

## Security Considerations

### File Upload Security
- File type validation using allowed extensions
- Secure filename handling with Werkzeug
- Temporary file isolation in dedicated directory
- Automatic cleanup of temporary files

### Input Validation
- File size limits (16MB default)
- Extension whitelist for supported formats
- Filename sanitization to prevent path traversal

### Error Handling
- Graceful error handling with user-friendly messages
- No sensitive information exposed in error responses
- Proper HTTP status codes for different error types

## Performance Considerations

### File Processing
- Temporary file storage for large documents
- Memory-efficient streaming for file operations
- Automatic cleanup to prevent disk space issues

### Concurrent Users
- Flask development server (single-threaded)
- Suitable for local/development use
- Production deployment would require WSGI server

### Resource Management
- Process management in launcher
- Signal handling for graceful shutdown
- Timeout handling for long-running operations

## Configuration

### Environment Variables
- No external configuration required
- All settings in application code
- Port and host configurable in main block

### File System
- Upload directory: `uploads/`
- Output directory: `outputs/`
- Automatic directory creation
- Git-ignored temporary files

## Dependencies

### Core Dependencies
- **Flask 3.0.0**: Web framework
- **MarkItDown 0.1.3**: Document conversion library
- **Werkzeug 3.0.1**: WSGI utilities
- **python-dotenv >=1.0.1**: Environment management

### MarkItDown Extensions
The application uses `markitdown[all]` which includes:
- PDF processing capabilities
- Microsoft Office document support
- HTML and text format handling
- Audio transcription features
- Azure Document Intelligence integration

## Error Handling

### Client-Side Errors
- File validation before upload
- User feedback for unsupported formats
- Loading states during conversion
- Error message display

### Server-Side Errors
- Exception handling in conversion process
- Graceful degradation for unsupported files
- Proper HTTP status codes
- Logging for debugging (in development mode)

## Browser Compatibility

### Supported Browsers
- Modern browsers with ES6 support
- Drag and drop API support
- Fetch API for AJAX requests
- Clipboard API for copy functionality

### Progressive Enhancement
- Basic file upload without JavaScript
- Enhanced experience with modern browser features
- Fallback for older browsers

## Deployment Considerations

### Development
- Flask development server
- Debug mode enabled
- Hot reloading for development

### Production
- WSGI server required (Gunicorn, uWSGI)
- Static file serving optimization
- Process management (systemd, supervisor)
- Reverse proxy configuration (nginx)

### Docker
- Containerization possible
- Volume mounts for file storage
- Port mapping for web access
- Health check endpoints

## Monitoring and Logging

### Health Checks
- `/health` endpoint for monitoring
- Process status verification
- Dependency availability checks

### Logging
- Flask built-in logging
- Error tracking in development
- Production logging configuration needed

## Testing

### Manual Testing
- File upload and conversion
- Error condition handling
- Browser compatibility
- Performance with large files

### Automated Testing
- Unit tests for conversion logic
- Integration tests for API endpoints
- End-to-end tests for user workflows

## Maintenance

### Regular Tasks
- Dependency updates
- Security patches
- Performance monitoring
- Log rotation

### Backup Considerations
- No persistent data storage
- Temporary file cleanup
- Configuration backup
- Code repository maintenance
