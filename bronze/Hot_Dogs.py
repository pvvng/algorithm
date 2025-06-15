while True:
  try :
    x, y = map(int, input().split())
    z = f"{x/y:.2f}"
    print(z)
  except EOFError:
    break