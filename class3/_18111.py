import sys
input = sys.stdin.readline

n, m, b = map(int, input().split())
G = [list(map(int, input().split())) for _ in range(n)]

time = float("inf")
hlevel = 0

# 가능한 모든 높이 확인
for h in range(257):
  use_block = 0
  take_block = 0

  for i in range(n):
    for j in range(m):
      if G[i][j] > h:
        take_block += G[i][j] - h
      else:
        use_block += h - G[i][j]

  if use_block > take_block + b:
    continue

  count = take_block * 2 + use_block

  if count <= time:
    time = count
    hlevel = h
  
print(time, hlevel)
