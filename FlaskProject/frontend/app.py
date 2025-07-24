from flask import Flask,render_template,request
from datetime import datetime
import requests

app = Flask(__name__)

BACKEND_URL = "http://0.0.0.0:8000"
@app.route('/')
def home():
    day_of_week = datetime.today().strftime('%A')
    current_time = datetime.now().time()

    return render_template('index.html',day_of_week_= day_of_week,current_time_=current_time)

@app.route('/submit',methods=['POST'])
def submit():
    form_data = dict(request.form)
    requests.post(BACKEND_URL+'/submit', data = form_data)
    return "success!!!"

@app.route('/get_data')
def get_data():
    response = requests.get(BACKEND_URL+'/view')
    return response.json()

if __name__ == "__main__":
    app.run(host='0.0.0.0',port=9000,debug=True)
