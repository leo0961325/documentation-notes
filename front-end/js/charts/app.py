
from flask import Flask, render_template, jsonify
from pymongo import MongoClient
import pymongo


app = Flask(__name__)
import json


@app.route('/')
def index():
    # return "<h1>test</h1>"
    return render_template('chartjs_barChart')

@app.route('/d3')
def d3():
    return render_template('d3Example1.html')

@app.route('/charts')
def charts():
    # o = {"cols": [{"id":"","label":"Topping","pattern":"","type":"string"},{"id":"","label":"Slices","pattern":"","type":"number"}],"rows": [{"c":[{"v":"Mushrooms","f":""},{"v":3,"f":""}]},{"c":[{"v":"Onions","f":""},{"v":1,"f":""}]},{"c":[{"v":"Olives","f":""},{"v":1,"f":""}]},{"c":[{"v":"Zucchini","f":""},{"v":1,"f":""}]},{"c":[{"v":"Pepperoni","f":""},{"v":2,"f":""}]}]}
    
    # return json.dumps(o)
    user = 'admin'
    host = '127.0.0.1'
    port = 27017
    host = 'mongodb://' + host + '/' + user
    db = MongoClient(host).pome
    cursor = db.dataNode.find().sort('_id', pymongo.DESCENDING).limit(1)
    cursor = db.randTime.find().sort('_id', pymongo.DESCENDING).limit(1)
    y = []
    x = []
    for d in cursor:
        # return([d['_id'], d['value']])
        x.append(d['_id'])
        y.append(d['value'])


    return jsonify( {'x': x, 'y': y} )
    # return [x, y]


###


if __name__ == '__main__':
    app.run(debug=True)