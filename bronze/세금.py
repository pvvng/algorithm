n = int(input())

def tax(x: int, dt: int = 22): 
  return int(x * (100 - dt) / 100)
def percent(x: int, dt: int):
  return int(x * dt / 100)

print(tax(n), percent(n, 80) + tax(percent(n, 20)))
