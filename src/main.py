from flask import Flask
from flask import request
from flask import send_file
from supermarket import * 
app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/superRoute')
def superRoute():
    target = request.args.get('target')
    name = request.args.get('name')
    superMarketRoute(int(target), name)
    basePath = os.path.abspath(os.path.join(__file__, '..', '..', 'output'))
    return send_file(basePath + '/' + name + '.png', mimetype='image/png')

if __name__ == '__main__':
    app.run()