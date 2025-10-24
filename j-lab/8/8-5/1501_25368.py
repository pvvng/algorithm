import sys
input = sys.stdin.readline

def in_range(r, c):
  return 0 <= r <= 4 and 0 <= c <= 4

def sol(board: list, aloc: tuple, bloc: tuple):
  visited = [[False] * 5 for _ in range(5)]
  remained_apple = 0
  for i in range(5):
    for j in range(5):
      if board[i][j] == -1:
        visited[i][j] = True
      remained_apple += max(0, board[i][j])

  return dfs(board, visited, remained_apple, aloc, bloc, 0)
      
def dfs(board, visited, remained_apple, cur, other, apple_diff):
  # 두 플레이어 모두 움직일 수 없을 때
  if visited[cur[0]][cur[1]] and visited[other[0]][other[1]]:
    return int(apple_diff > 0)

  # 남은 사과가 없을 때
  if remained_apple == 0:
    return int(apple_diff > 0)

  dt = [(0,1), (0,-1), (1,0), (-1,0)]
  moved = False
  for dr, dc in dt:
    nr, nc = cur[0] + dr, cur[1] + dc
    if in_range(nr, nc) and not visited[nr][nc] and (nr, nc) != other:
      moved = True
      # 현재 위치 처리
      visited[cur[0]][cur[1]] = True
      nxt_val = max(0, board[cur[0]][cur[1]])
      # 턴 바꿔서 플레이
      ret = dfs(board, visited, remained_apple - nxt_val, other, (nr, nc), -(apple_diff + nxt_val))
      visited[nr][nc] = False

      # 다음 차례 플레이어의 패배
      if ret == 0:
        return 1

  # 현재 플레이어가 움직일 수 없었다면
  if not moved:
    # 턴을 바꿔서 플레이
    prev = visited[cur[0]][cur[1]]
    visited[cur[0]][cur[1]] = True
    ret = dfs(board, visited, remained_apple, other, cur, -apple_diff)
    visited[cur[0]][cur[1]] = prev

    if ret == 0:
      return 1

  # 어떤 경우에도 승리 불가
  return 0

board = [list(map(int, input().split())) for _ in range(5)]
r1, c1, r2, c2 = map(int, input().split())
print(sol(board, (r1, c1), (r2, c2)))