from flask import Flask,render_template
import requests
import os

PORT = os.environ.get('PORT', 9000)
Backend_URL = os.environ.get('Backend_URL', 'http://localhost:8000')

app = Flask(__name__)

@app.route('/')
def home():
    
    response = requests.get(f"{Backend_URL}/api/get")

    data = response.json()

    env = dict(os.environ)

    return render_template('index.html',env = env,data=data['data'])

if __name__ == '__main__':
    app.run(debug=True,port=PORT,host='0.0.0.0')