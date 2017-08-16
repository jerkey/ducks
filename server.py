import cart
from bottle import route, run, template

@route('/')
def index():
  return template('<b>Hello</b>!')

@route('/cart/<cmd>')
def cart_off(cmd):
  if not hasattr(cart, cmd):
    return template('NOPE')

  getattr(cart, cmd)()
  return template('OK')

cart.unexport()
cart.export()
run(host='localhost', port=8080)
