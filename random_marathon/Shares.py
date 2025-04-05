while True:
  try:
    n, m = map(int, input().split())
  except(EOFError):
    break
  else:
    print(m//(n+1))

