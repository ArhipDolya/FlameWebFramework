from re import match
from webob import Request, Response
from parse import parse

import re


class Flame:

    def __init__(self):
        self.routes = {}

    def __call__(self, environ, start_response):
        request = Request(environ)
        response = self.handle_request(request)
        return response(environ, start_response)

    def add_route(self, path, handler):
        self.routes[path] = handler

    def route(self, path):
        def decorator(handler):
            self.routes[path] = handler
            return handler
        return decorator

    def find_handler(self, request_path):
        for route_pattern, handler in self.routes.items():
            parse_result = parse(route_pattern, request_path)
            if parse_result is not None:
                return handler, parse_result.named
        return None, None

    def handle_request(self, request):
        response = Response()
        handler, kwargs = self.find_handler(request_path=request.path)

        if handler is not None:
            try:
                handler(request, response, **kwargs)
            except Exception as e:
                response.status_code = 500
                response.text = f"Internal Server Error: {str(e)}"
        else:
            response.status_code = 404
            response.text = 'Page Not Found'

        return response