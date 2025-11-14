n = int(input())

ans = []
for i in range(n):
  b = 2 * i
  s = 2 * n - 1
  ans.append(" " * (b // 2) + "*" * (s - b))
print("\n".join(ans))
