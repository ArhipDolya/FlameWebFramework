from flame import Flame
from waitress import serve


app = Flame()


@app.route('/')
def hi(request, response):
    response.text = f'Hi'


@app.route('/hello/{name}')
def hello(request, response, name):
    response.text = f'Hello, {name}'


@app.route('/goodbye/{name}')
def goodbye(request, response, name):
    response.text = f'Goodbye, {name}'


@app.route('/about')
@app.route('/about/')
def about(request, response):
    response.text = 'Page about us'


if __name__ == '__main__':
    serve(app, host='0.0.0.0', port=8000)