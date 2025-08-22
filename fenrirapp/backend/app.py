from flask import Flask,render_template,jsonify
from connections import coll
import os

PORT = os.getenv('PORT', 8000)

app = Flask(__name__)

@app.route('/')
def home():
    return jsonify({"message":"Backend is running"})

@app.route('/api/get')
def api():
    names = coll.find()
    res = []

    for name in names:
        res.append(name['value'])

    res = {
        'data' : res
    }
    
    return jsonify(res)

@app.route('/api/add/<name>')
def add(name):
    coll.insert_one({'value':name})
    return jsonify({"message":f"{name} Added"})

if __name__ == '__main__':
    app.run(debug=True,port=PORT,host='0.0.0.0')