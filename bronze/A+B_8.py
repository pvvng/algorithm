x = int(input())

for i in range(1, x+1):
  n, m = map(int, input().split())
  print(f"Case #{i}: {n} + {m} = {m+n}")