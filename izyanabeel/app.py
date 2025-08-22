from flask import Flask,render_template
import os

PORT = os.getenv('PORT', 8000)

app = Flask(__name__)

@app.route('/')
def home():
    env = dict(os.environ)
    return render_template('index.html',env = env)

if __name__ == '__main__':
    app.run(debug=True,port=PORT,host='0.0.0.0')