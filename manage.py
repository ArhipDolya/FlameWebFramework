from flame import Flame
from waitress import serve
from webob import Request, Response


app = Flame()


@app.route('/')
def hello(request):
    return Response(text=f'Hello, world!')


@app.route('/goodbye')
def goodbye(request):
    return Response(text='GoodBye, world!')


if __name__ == '__main__':
    serve(app, host='0.0.0.0', port=8000)