import dis

# M1
def bar():
  a, b = 1, 2
  print(a, b) # 结果：2 1
  a, b = b, a
  print(a, b)

dis.dis(bar)

# M2
def swap2(a=1, b=2):
  temp = a
  a = b
  b = temp
  print(a, b)

swap2()

# M3
def swap3(a=1, b=2):
  a = a + b
  b = a - b
  a = a - b
  print(a, b)

swap3()

# M4
def swap4(a=1, b=2):
  a = a ^ b
  b = a ^ b
  a = a ^ b
  print(a, b)

swap4()