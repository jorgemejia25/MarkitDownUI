#!/usr/bin/env python3
"""
MarkItDown Application Launcher

A comprehensive launcher for the MarkItDown web application that handles
dependency installation, server startup, browser opening, and cleanup.

This launcher provides a user-friendly way to start the MarkItDown application
with automatic dependency checking, server management, and browser integration.

Author: jorgemejia25
Version: 1.0.0
"""

import os
import sys
import subprocess
import webbrowser
import time
import signal
import threading
from pathlib import Path


class MarkItDownLauncher:
    """
    Main launcher class for the MarkItDown application.
    
    Handles the complete lifecycle of the application including:
    - Dependency verification and installation
    - Server startup and management
    - Browser integration
    - Cleanup and shutdown
    """
    
    def __init__(self):
        """
        Initialize the MarkItDown launcher.
        
        Sets up the application directory, port configuration,
        and process management variables.
        """
        self.app_process = None
        self.port = 5001
        self.app_dir = Path(__file__).parent
        
    def check_dependencies(self):
        """
        Verify that all required dependencies are installed.
        
        Checks for Flask and MarkItDown imports. If dependencies are missing,
        attempts to install them from requirements.txt.
        
        Returns:
            bool: True if dependencies are available, False otherwise
        """
        try:
            import flask
            import markitdown
            print("Dependencias verificadas")
            return True
        except ImportError as e:
            print(f"Error: {e}")
            print("Instalando dependencias...")
            try:
                subprocess.run([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"], 
                             check=True, cwd=self.app_dir)
                print("Dependencias instaladas correctamente")
                return True
            except subprocess.CalledProcessError:
                print("Error al instalar dependencias")
                return False
    
    def start_server(self):
        """
        Start the Flask server process.
        
        Changes to the application directory and starts the Flask server
        as a subprocess. Waits for the server to initialize and verifies
        it's running properly.
        
        Returns:
            bool: True if server started successfully, False otherwise
        """
        try:
            print(f"Iniciando servidor en puerto {self.port}...")
            
            # Change to application directory
            os.chdir(self.app_dir)
            
            # Start Flask server
            self.app_process = subprocess.Popen([
                sys.executable, "app.py"
            ], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            
            # Wait for server to initialize
            time.sleep(3)
            
            # Verify server is running
            if self.app_process.poll() is None:
                print("Servidor iniciado correctamente")
                return True
            else:
                print("Error al iniciar el servidor")
                return False
                
        except Exception as e:
            print(f"Error: {e}")
            return False
    
    def open_browser(self):
        """
        Open the default web browser with the application URL.
        
        Attempts to open the MarkItDown application in the user's
        default web browser at the configured port.
        """
        try:
            url = f"http://localhost:{self.port}"
            print(f"Abriendo navegador en {url}")
            webbrowser.open(url)
            print("Navegador abierto")
        except Exception as e:
            print(f"Error al abrir navegador: {e}")
    
    def wait_for_user(self):
        """
        Wait for user input to close the application.
        
        Displays status information and waits for the user to press
        Enter or send a keyboard interrupt to close the application.
        """
        print("\n" + "="*50)
        print("MarkItDown está ejecutándose")
        print(f"Abre tu navegador en: http://localhost:{self.port}")
        print("Convierte tus documentos a Markdown")
        print("="*50)
        print("\nPresiona ENTER para cerrar la aplicación...")
        
        try:
            input()
        except KeyboardInterrupt:
            pass
    
    def cleanup(self):
        """
        Clean up resources when closing the application.
        
        Terminates the Flask server process gracefully, with a fallback
        to force kill if the process doesn't respond to termination.
        """
        if self.app_process:
            print("\nCerrando servidor...")
            self.app_process.terminate()
            try:
                self.app_process.wait(timeout=5)
            except subprocess.TimeoutExpired:
                self.app_process.kill()
            print("Servidor cerrado")
    
    def run(self):
        """
        Run the complete MarkItDown application.
        
        Orchestrates the entire application lifecycle:
        1. Check and install dependencies
        2. Start the Flask server
        3. Open the web browser
        4. Set up signal handlers for cleanup
        5. Wait for user input to close
        6. Clean up resources
        """
        print("MarkItDown Launcher")
        print("="*30)
        
        # Check dependencies
        if not self.check_dependencies():
            return
        
        # Start server
        if not self.start_server():
            return
        
        # Open browser
        self.open_browser()
        
        # Set up signal handlers for cleanup
        def signal_handler(signum, frame):
            self.cleanup()
            sys.exit(0)
        
        signal.signal(signal.SIGINT, signal_handler)
        signal.signal(signal.SIGTERM, signal_handler)
        
        try:
            # Wait for user to close application
            self.wait_for_user()
        finally:
            self.cleanup()


if __name__ == "__main__":
    """
    Main entry point for the MarkItDown launcher.
    
    Creates and runs the launcher instance when the script is executed directly.
    """
    launcher = MarkItDownLauncher()
    launcher.run()
