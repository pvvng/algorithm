a, b = map(int, input().split())
items = list(map(int, input().split()))
ans = []
for i in items:
  ans.append(str(i - (a*b)))
print(" ".join(ans))