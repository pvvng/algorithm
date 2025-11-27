import sys
input = sys.stdin.readline

n = int(input())
A = [tuple(map(int, input().split())) for _ in range(n)]
A.sort(key=lambda x: (x[1], x[0]))

ans = 1
prev = A[0][1]
for i in range(1, n):
  start, end = A[i]
  if start >= prev:
    ans += 1
    prev = end

print(ans)