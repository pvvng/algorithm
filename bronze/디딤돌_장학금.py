M = list(map(int, input().split()))
n = int(input())
ans = 0
for _ in range(n):
  b, l, s = map(float, input().split())
  if l < 2.0 or s < 17:
    continue
  ans += M[int(b)]
print(ans)
