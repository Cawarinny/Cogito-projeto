import compass as cp
from flask import Flask

app = Flask('Bussola')

@app.route('/compass')
def compassApi():
    dadosGraphic = cp.compass()
    return dadosGraphic

app.run()
