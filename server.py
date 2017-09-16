from bottle import route, run, auth_basic, redirect, request
from subprocess import call

import duckfavicon

authfile = open('authfile','r') # first line of file is login, second is password
lines=authfile.readlines()

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
  call(["duckopen &"],shell=True)
  return redirect('/?lastCommand=open')

@route('/ducks/close')
@auth_basic(check)
def ducks_close():
  call(["duckclose &"],shell=True)
  return redirect('/?lastCommand=closed')

@route('/ducks/stop')
@auth_basic(check)
def ducks_stop():
  call(["duckstop"],shell=True)
  return redirect('/?lastCommand=stopped')

run(host='0.0.0.0', port=8100)
