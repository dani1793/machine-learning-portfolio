from flask import Flask, request, jsonify, abort
from extraction import extract
app = Flask(__name__)

graph = extract()

@app.route("/nearest")
def nearest():
     id = request.args.get('id')
     try:
        if(id is None):
            abort(400)
        neighbours = graph.getNeighbours(int(id))
        return jsonify({"nearest": neighbours})
     except Exception as error:
        return error
     
@app.route("/path")
def path():
    id1 = request.args.get('id1')
    id2 = request.args.get('id2')
    try: 
        if(id1 is None or id2 is None):
            abort(400)
        path = graph.aStartSearch(int(id1), int(id2))
        return jsonify({"path": path})
    except Exception as error:
        return error

    
