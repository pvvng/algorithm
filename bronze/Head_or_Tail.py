while True:
  n = int(input())
  if n == 0:
    break
  d = { 0: 0, 1: 0 }
  ls = list(map(int, input().split()))
  for e in ls:
    d[e] += 1
  print(f"Mary won {d[0]} times and John won {d[1]} times")