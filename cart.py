import gpio

left = 22
dir1 = 23
right = 24
dir2 = 25

def unexport():
  gpio.unexport(left)
  gpio.unexport(right)
  gpio.unexport(dir2)
  gpio.unexport(dir1)

def export():
  gpio.export(left)
  gpio.export(right)
  gpio.export(dir2)
  gpio.export(dir1)

def forward():
  gpio.write(dir1, 0)
  gpio.write(dir2, 0)
  gpio.on(left)
  gpio.on(right)

def backward():
  gpio.write(dir1, 1)
  gpio.write(dir2, 1)
  gpio.on(left)
  gpio.on(right)

def stop():
  gpio.off(left)
  gpio.off(right)

