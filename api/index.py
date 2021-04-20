import compass as cp
from flask import Flask

app = Flask(__name__)

@app.route('/compass')
def compassApi():
    dadosGraphic = cp.compass()
    return dadosGraphic

app.run()