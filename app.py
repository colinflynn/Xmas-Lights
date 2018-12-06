from flask import Flask, render_template
from src.lightController import LightController
import json

app = Flask(__name__)
lightController = LightController()

@app.route('/')
def index():
    lightController.lightsWhite()
    return render_template('index.html', current_color='White')

@app.route('/red')
def red():
    lightController.lightsRed()
    return render_template('index.html', current_color='Red')

@app.route('/rainbow')
def rainbow():
    lightController.lightsRainbow()
    return render_template('index.html', current_color='Rainbow')

@app.route('/redwhite')
def redWhite():
    lightController.lightsRedWhite()
    return render_template('index.html', current_color='Red and White')

@app.route('/redwhitegreen')
def redWhiteGreen():
    lightController.lightsRedWhiteGreen()
    return render_template('index.html', current_color='Red White and Green')

@app.route('/off')
def off():
    lightController.lightsOff()
    return render_template('index.html', current_color='No')

try:
    app.run(debug=True,use_reloader=False,host='0.0.0.0')
except Exception as err:
    print err