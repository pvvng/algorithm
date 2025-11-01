ans = []
for _ in range(int(input())):
  a, b, x = map(int, input().split())
  ans.append(str(a * (x - 1) + b))

print("\n".join(ans))