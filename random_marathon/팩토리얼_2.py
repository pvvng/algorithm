value = int(input())

def fac (value):
  if(value <= 1) :
    return 1
  return value * fac (value - 1)

print(fac(value))