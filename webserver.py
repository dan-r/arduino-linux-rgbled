from flask import Flask, current_app, abort, request
import serial
import re
import time
ser = serial.Serial('/dev/ttyUSB0',9600)
app = Flask(__name__)

@app.route('/')
def index():
    return current_app.send_static_file('remote.html');

@app.route('/favicon.ico')
def favicon():
    abort(404);

@app.route('/<path:path>')
def catch_all(path):
    global lcd1, lcd11, lcd2, lcd21
    states = ['on', 'off']
    colours = ['r','r1','r2','r3','r4','g','g1','g2','g3','g4','b1','b2','b3','b4','w','fade','smooth','strobe','flash']
    if any(path in s for s in states):
        ser.write(path+"\n")
    elif any(path in s for s in colours):
        ser.write("on\n")
        time.sleep(0.15);
        ser.write(path+"\n")
        time.sleep(0.15);
    else:
        ser.write(path+"\n")
    return 'done'

if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0')