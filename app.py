from flask import Flask,request,jsonify
from api import generate
from dotenv import load_dotenv
import json
import os

# load secret
load_dotenv()

app = Flask(__name__)
app.config['API_KEY'] = os.getenv('API_KEY')

@app.route('/')
def home():
    return 'Hello, Flask!'

@app.route('/api',methods=["POST"])
def api():
    data = json.loads(request.get_data())
    return generate(data['phrase'])

if __name__ == '__main__':
    app.run(debug=True)

