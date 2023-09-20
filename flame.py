from webob import Request, Response


class Flame:

    def __init__(self):
        self.routes = []

    def add_route(self, path, handler):
        self.routes.append((path, handler))

    def route(self, path):
        def decorator(handler):
            self.add_route(path, handler)
            return handler
        return decorator

    def __call__(self, environ, start_response):
        request = Request(environ)
        response = self.handle_request(request)
        return response(environ, start_response)

    def handle_request(self, request):
        for path, handler in self.routes:
            if request.path_info == path:
                return handler(request)

        return Response(status=404, text='Page Not Found')