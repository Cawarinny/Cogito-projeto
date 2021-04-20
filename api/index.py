import loop
from flask import Flask

app = Flask(__name__)

@app.route('/compass')
def compassApi():
    dadosGraphic = loopCompass()
    return dadosGraphic

app.run()
