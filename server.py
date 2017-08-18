import cart
from bottle import route, run

@route('/')
def index():
  return '<b>Hello</b>!'

@route('/cart/<cmd>')
def cart_off(cmd):
  if not hasattr(cart, cmd):
    return 'NOPE'

  getattr(cart, cmd)()
  return 'OK'

run(host='0.0.0.0', port=8100)
