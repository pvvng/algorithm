n = int(input())
ans = []
for i in range(1, n+1):
  ans.append(" " * (n - i) + "*" * (2 * i - 1))
print("\n".join(ans))