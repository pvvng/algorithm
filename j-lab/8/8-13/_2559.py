import sys
input = sys.stdin.readline

n, k = map(int, input().split())
D = list(map(int, input().split()))

# 누적합
for i in range(1, n):
  D[i] += D[i-1]

ans = D[k-1]
for i in range(1, n-k+1):
  ret = D[i+k-1] - D[i-1]
  if ret > ans:
    ans = ret

print(ans)