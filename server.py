from bottle import route, run, auth_basic, redirect, request

import duckfavicon, serial
import datetime

arduino = serial.Serial(port='/dev/serial/by-id/usb-Arduino__www.arduino.cc__0043_A41323739353519050D0-if00', baudrate=9600)

authfile = open('authfile','r') # first line of file is login, second is password
lines=authfile.readlines()
logfile = open('/tmp/ducks.log','wa') # open logfile for appending

def check(user, pw):
  if user == lines[0].strip() and pw == lines[1].strip():
    return True
  else:
    return False

hello=duckfavicon.favicon+'''
    <style> td, a { text-decoration: none; font-size: 4em; padding: 10px; } table, .btn { display: block; }
    .open { background-color: green; } .stop{ background-color: red; } .close{ background-color: yellow; }
    </style><table>
    <tr><td><a class='btn open' href=/ducks/open>open</a></td>
        <td><a class='btn stop' href=/ducks/stop>stop</a></td></tr>
        <td><a class='btn close' href=/ducks/close>close</a></td></tr>
    <tr><td>$D</td><td>$D</td></tr>
    <tr><td>door position is</td><td>$D</td></tr>
    </table>
'''

@route('/favicon.ico')
def fav_serve():
  return duckfavicon.favicon

@route('/')
@auth_basic(check)
def index():
  lastCommand = request.query.get('lastCommand', '')
  return lastCommand+hello

@route('/ducks/open')
@auth_basic(check)
def ducks_open():
  arduino.write('1')
  logfile.write(str(datetime.datetime.today())+' OPEN\n')
  logfile.flush()
  return redirect('/?lastCommand=open')

@route('/ducks/close')
@auth_basic(check)
def ducks_close():
  arduino.write('2')
  logfile.write(str(datetime.datetime.today())+' CLOSE\n')
  logfile.flush()
  return redirect('/?lastCommand=closed')

@route('/ducks/stop')
@auth_basic(check)
def ducks_stop():
  arduino.write('0')
  logfile.write(str(datetime.datetime.today())+' STOP\n')
  logfile.flush()
  return redirect('/?lastCommand=stopped')

@route('/ducks/test')
@auth_basic(check)
def ducks_test():
  arduino.write('t') # t doesn't do anything, we're just testing serial write
  logfile.write(str(datetime.datetime.today())+' TEST\n')
  logfile.flush()
  return redirect('/?lastCommand=tested')

logfile.write(str(datetime.datetime.today())+' server initialized\n')
run(host='0.0.0.0', port=8100)
