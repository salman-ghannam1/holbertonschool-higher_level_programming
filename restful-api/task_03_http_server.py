#!/usr/bin/python3
"""Module to implement http.server module"""

import http.server
import json


class HTTPHandler(http.server.BaseHTTPRequestHandler):
    """Simple Handler class inherited from BaseHTTPRequestHandler"""

    def _set_headers(self, status=200, content_type='text/plain'):
        """Reusable method for sending headers"""
        self.send_response(status)
        self.send_header('Content-type', content_type)
        self.end_headers()

    def do_GET(self):
        """Method to handle GET requests"""

        if self.path == '/':
            self._set_headers(content_type='text/plain')
            self.wfile.write(b"Hello, this is a simple API!")

        elif self.path == '/data':
            self._set_headers(content_type='application/json')
            data = {
                "name": "John",
                "age": 30,
                "city": "New York"
            }
            self.wfile.write(json.dumps(data).encode('utf-8'))

        elif self.path == '/status':
            self._set_headers(content_type='text/plain')
            self.wfile.write(b"OK")

        elif self.path == '/info':
            self._set_headers(content_type='application/json')
            data = {
                "version": "1.0",
                "description": "A simple API built with http.server"
            }
            self.wfile.write(json.dumps(data).encode('utf-8'))

        else:
            self.send_response(404)
            self.send_header("Content-type", "text/plain")
            self.end_headers()
            self.wfile.write(b"FAIL - Undefined endpoint ")

if __name__ == '__main__':
    """Server initialization"""
    server_address = ("", 8000)
    httpserver = http.server.HTTPServer(server_address, HTTPHandler)
    print("Server running at http://localhost:8000")
    httpserver.serve_forever()
