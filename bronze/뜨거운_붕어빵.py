n, m = map(int,input().split())
for _ in range(n):
  x = list(input())
  x.reverse()
  print("".join(x))