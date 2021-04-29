import os
import compass as cp
from flask import Flask
from flask_cors import CORS, cross_origin

app = Flask(__name__)

@app.route('/')
@cross_origin()
def compassApi():
    dadosGraphic = cp.compass()
    return dadosGraphic

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
