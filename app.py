from flask import Flask, render_template
from src.lightController import LightController
import threading
import json

app = Flask(__name__)
lightController = LightController()

@app.route('/')
def off():
    lightController.lightsOff()
    return render_template('index.html', current_color='No')

@app.route('/white')
def white():
    thread = threading.Thread(target=whiteThread)
    thread.start()
    return render_template('index.html', current_color='White')

@app.route('/red')
def red():
    thread = threading.Thread(target=redThread)
    thread.start()
    return render_template('index.html', current_color='Red')

@app.route('/redwhite')
def redWhite():
    thread = threading.Thread(target=redWhiteThread)
    thread.start()
    return render_template('index.html', current_color='Red and White')

@app.route('/redwhitegreen')
def redWhiteGreen():
    thread = threading.Thread(target=redWhiteGreenThread)
    thread.start()
    return render_template('index.html', current_color='Red White and Green')

@app.route('/rainbow')
def rainbow():
    thread = threading.Thread(target=rainbowThread)
    thread.start()
    return render_template('index.html', current_color='Rainbow')

def whiteThread():
    lightController.lightsWhite()

def redThread():
    lightController.lightsRed()

def redWhiteThread():
    lightController.lightsRedWhite()

def redWhiteGreenThread():
    lightController.lightsRedWhite()

def rainbowThread():
    lightController.lightsRainbow()

try:
    app.run(debug=True,use_reloader=False,host='0.0.0.0')
except Exception as err:
    print err