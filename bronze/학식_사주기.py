n = int(input())
N = [int(input()) for _ in range(n)]
m = int(input())
ans = 0
for _ in range(m):
  ans += N[int(input()) - 1]
print(ans)
