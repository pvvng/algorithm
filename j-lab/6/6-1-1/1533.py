def in_range(r, c):
  return 0 <= r <= 4 and 0 <= c <= 4

def is_not_visited(r, c, visited):
  return (r, c) not in visited

def sol(board:list, queue: list, visited: set):
  dt = [(0,1),(0,-1),(1,0),(-1,0)]
  
  idx = 0
  while idx < len(queue):
    crt = queue[idx]
    visited.add((crt[0], crt[1]))
    idx += 1

    if board[crt[0]][crt[1]] == 1:
      return crt[2]

    for d in dt:
      nr, nc = crt[0]+d[0], crt[1]+d[1]
      dist = crt[2]
      # 조기 종료
      if in_range(nr, nc) and board[nr][nc] == 1:
        return dist + 1
      if in_range(nr, nc) and board[nr][nc] != -1 and is_not_visited(nr, nc, visited):
        queue.append((nr, nc, dist + 1))

  return -1

board = [list(map(int, input().split())) for _ in range(5)]
r, c = map(int, input().split())
print(sol(board, [(r, c, 0)], set()))