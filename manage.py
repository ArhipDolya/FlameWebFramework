from flame import Flame
from waitress import serve
from webob import Request, Response


app = Flame()


@app.route('/')
def hello(request):
    return Response(text=f'Hello, world!')


@app.route('/hello/{name}')
def hello(request, response, name):
    response.text = f'Hello, {name}'


@app.route('/goodbye/{name}')
def goodbye(request, response, name):
    response.text = f'Goodbye, {name}'
    #return Response(text='GoodBye, world!')


@app.route('/about')
@app.route('/about/')
def about(request):
    return Response(text='Page about us')


if __name__ == '__main__':
    serve(app, host='0.0.0.0', port=8000)