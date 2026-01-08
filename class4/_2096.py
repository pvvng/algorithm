import sys
input = sys.stdin.readline

n = int(input())
# 첫줄 입력
a, b, c = map(int, input().split())
prev = [[a, a], [b, b], [c, c]]
cur = [[0, 0] for _ in range(3)]
for _ in range(n-1):
  line = list(map(int, input().split()))
  # c = 0
  cur[0][0] = line[0] + max(prev[0][0], prev[1][0])
  cur[0][1] = line[0] + min(prev[0][1], prev[1][1])
  # c = 1
  cur[1][0] = line[1] + max(prev[0][0], prev[1][0], prev[2][0])
  cur[1][1] = line[1] + min(prev[0][1], prev[1][1], prev[2][1])
  # c = 2
  cur[2][0] = line[2] + max(prev[1][0], prev[2][0])
  cur[2][1] = line[2] + min(prev[1][1], prev[2][1])

  prev, cur = cur, prev

mx = max(prev[i][0] for i in range(3))
mn = min(prev[i][1] for i in range(3))

print(mx, mn)