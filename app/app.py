from flask import Flask, jsonify, request
from datetime import datetime

app = Flask(__name__)

@app.route('/', defaults={'path': ''}, methods=['GET', 'POST', 'PUT', 'DELETE'])
@app.route('/<path:path>', methods=['GET', 'POST', 'PUT', 'DELETE'])
def home(path):
   now = datetime.now()

   dt = {}
   dt["date"] = now.strftime("%d/%m/%Y")
   dt["time"] = now.strftime("%H:%M:%S")

   return jsonify(dt)

if __name__ == "__main__":
	app.run()
