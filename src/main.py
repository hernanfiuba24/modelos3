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
    targets = map(int, request.args.get('target').split(","))
    name = request.args.get('superName')
    graphName = name + 'Graph'
    sourcesToCash = []
    if name == 'hallways':
        sourcesToCash = [21, 22] # cashbox
    if name == 'hallwaysSuperX':
        sourcesToCash = [5, 6] # cashbox
    superMarketRoute(targets, name, graphName, sourcesToCash)
    basePath = os.path.abspath(os.path.join(__file__, '..', '..', 'output'))
    return send_file(basePath + '/' + name + '.png', mimetype='image/png')

@app.route('/hallwaysSuper/<path:hallwaysName>')
def hallways(hallwaysName):
    hallwaysSuper(hallwaysName, hallwaysName + 'Graph')
    basePath = os.path.abspath(os.path.join(__file__, '..', '..', 'output'))
    return send_file(basePath + '/' + hallwaysName + '.png', mimetype='image/png')

if __name__ == '__main__':
    app.run()