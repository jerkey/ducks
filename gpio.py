def export(gpio):
  f = open ('/sys/class/gpio/export','w')
  f.write(str(gpio))
  f.close()

  path = '/sys/class/gpio/gpio' + str(gpio) + '/direction'
  f = open (path,'w')
  f.write('out')
  f.close()

def unexport(gpio):
  try:
    f= open ('/sys/class/gpio/unexport','w')
    f.write(str(gpio))
    f.close()
  except IOError as e:
    lol=0

def write(gpio, value):
  path = '/sys/class/gpio/gpio' + str(gpio) + '/value'
  f= open (path,'w')
  f.write(str(value))
  f.close()

def on(gpio):
  write(gpio, '1')

def off(gpio):
  write(gpio, '0')

