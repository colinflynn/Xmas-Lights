from flask import Flask, render_template
from src.lightController import LightController
import json

app = Flask(__name__)
lightController = LightController()

@app.route('/')
def index():
    lightController.lightsWhite()
    return 'Lights White'

@app.route('/red')
def red():
    lightController.lightsRed()
    return 'Lights Red'

@app.route('/rainbow')
def rainbow():
    lightController.lightsRainbow()
    return 'Lights Rainbow'    

@app.route('/redwhite')
def redWhite():
    lightController.lightsRedWhite()
    return 'Lights Red and White'

@app.route('/redwhitegreen')
def redWhiteGreen():
    lightController.lightsRedWhiteGreen()
    return 'Lights Red, White, and Green'   

@app.route('/off')
def off():
    lightController.lightsOff()
    return 'Lights Off'

try:
    app.run(debug=True,use_reloader=False,host='0.0.0.0')
except Exception as err:
    print err