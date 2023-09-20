from flame import Flame
from waitress import serve

app = Flame()



if __name__ == '__main__':
    serve(app, host='0.0.0.0', port=8000)