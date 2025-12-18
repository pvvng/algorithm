import sys
input = sys.stdin.readline

n, m = map(int, input().split())

ladder = {}
for _ in range(n):
  x, y = map(int, input().split())
  ladder.setdefault(x, y)

snake = {}
for _ in range(m):
  x, y = map(int, input().split())
  snake.setdefault(x, y)

def bfs(ladder: dict, snake: dict):
  visited = [False] * 101

  q = [(1, 0)]
  idx = 0

  while idx < len(q):
    cur, move = q[idx]
    idx += 1

    if 94 <= cur <= 100:
      return move + 1
    
    snake_cur = snake.get(cur)
    if snake_cur:
      visited[snake_cur] = True
      q.append((snake_cur, move))
      continue

    ladder_cur = ladder.get(cur)
    if ladder_cur:
      visited[ladder_cur] = True
      q.append((ladder_cur, move))
      continue

    for i in range(1, 7):
      # 주사위 굴리기
      nxt = cur + i
      
      snake_nxt = snake.get(nxt)
      if snake_nxt:
        visited[snake_nxt] = True
        q.append((snake_nxt, move + 1))
        continue

      ladder_nxt = ladder.get(nxt)
      if ladder_nxt:
        visited[ladder_nxt] = True
        q.append((ladder_nxt, move + 1))
        continue

      if not visited[nxt]:
        q.append((nxt, move + 1))
        visited[nxt] = True

print(bfs(ladder, snake))
