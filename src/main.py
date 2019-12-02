from flask import Flask
from flask import request
from flask import Response
from flask import send_file
from flask import jsonify
from flask import make_response
from supermarket import * 
import json
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

@app.route('/hallwaysData/<path:hallwaysName>')
def hallwaysData(hallwaysName):
    basePath = os.path.abspath(os.path.join(__file__, '..', '..', 'files'))
    path = basePath + '/' + hallwaysName + '.json'
    print(path)
    with open(path) as json_file:
        data = json.load(json_file)
        response = make_response(jsonify(data))
        response.headers['access-control-allow-origin'] = '*'
        return response
    return {}

if __name__ == '__main__':
    app.run()