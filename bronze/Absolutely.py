for _ in range(int(input())):
  x, y = map(float, input().split())
  print(round(abs(x-y), 1))