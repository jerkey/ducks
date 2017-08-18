from bottle import route, run
from subprocess import call

hello='''
    <style> td, a { font-size: 4em; } table, .btn { display: block; }
    .open { background-color: green; } .stop{ background-color: red; } .close{ background-color: yellow; }
    </style><table>
    <tr><td><a class='btn open' href=/ducks/open>open</a></td>
        <td><a class='btn stop' href=/ducks/stop>stop</a></td></tr>
        <td><a class='btn close' href=/ducks/close>close</a></td></tr>
    <tr><td>$D</td><td>$D</td></tr>
    <tr><td>door position is</td><td>$D</td></tr>
    </table>
'''

lastCommand = 'none'
@route('/')
def index():
  return lastCommand+hello

@route('/ducks/open')
def ducks_open():
  call(["duckopen &"],shell=True)
  lastCommand = 'open'
  return lastCommand+hello

@route('/ducks/close')
def ducks_close():
  call(["duckclose &"],shell=True)
  lastCommand = 'closed'
  return lastCommand+hello

@route('/ducks/stop')
def ducks_stop():
  call(["duckstop"],shell=True)
  lastCommand = 'stopped'
  return lastCommand+hello

run(host='0.0.0.0', port=8100)
