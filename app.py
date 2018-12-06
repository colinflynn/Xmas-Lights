from flask import Flask, render_template
from src.lightController import LightController
import threading
import json

app = Flask(__name__)
lightController = LightController()


@app.route('/')
def off():
    lightController.lightsOff()
    return render_template('index.html', current_color='No', brightness=lightController.getLedBrightness())

@app.route('/white')
def white():
    thread = threading.Thread(target=whiteThread)
    thread.start()
    return render_template('index.html', current_color='White', brightness=lightController.getLedBrightness())

@app.route('/red')
def red():
    thread = threading.Thread(target=redThread)
    thread.start()
    return render_template('index.html', current_color='Red', brightness=lightController.getLedBrightness())

@app.route('/redwhite')
def redWhite():
    thread = threading.Thread(target=redWhiteThread)
    thread.start()
    return render_template('index.html', current_color='Red and White', brightness=lightController.getLedBrightness())

@app.route('/redwhitegreen')
def redWhiteGreen():
    thread = threading.Thread(target=redWhiteGreenThread)
    thread.start()
    return render_template('index.html', current_color='Red White and Green', brightness=lightController.getLedBrightness())

@app.route('/rainbow')
def rainbow():
    thread = threading.Thread(target=rainbowThread)
    thread.start()
    return render_template('index.html', current_color='Rainbow', brightness=lightController.getLedBrightness())

@app.route('/candycane')
def candyCanel():
    thread = threading.Thread(target=candyCaneThread)
    thread.start()
    return render_template('index.html', current_color='Candy Cane', brightness=lightController.getLedBrightness())

def whiteThread():
    lightController.lightsWhite()

def redThread():
    lightController.lightsRed()

def redWhiteThread():
    lightController.lightsRedWhite()

def redWhiteGreenThread():
    lightController.lightsRedWhiteGreen()

def rainbowThread():
    lightController.lightsRainbow()

def candyCaneThread():
    lightController.lightsCandyCane()

try:
    app.run(debug=True,use_reloader=False,host='0.0.0.0')
except Exception as err:
    print err