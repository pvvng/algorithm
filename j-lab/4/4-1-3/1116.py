# 백트래킹 사용 (내 풀이)

def is_in_range(r, c):
  return 0 <= r < 5 and 0 <= c < 5

def sol(loc:tuple, board:list, cnt:int, move:int):
  if cnt >= 2:
    return True
  if move == 3:
    return False

  (r, c) = loc
  temp = board[r][c]
  board[r][c] = -1  # 현재 위치 막기

  dt = [(-1, 0), (1, 0), (0, 1), (0, -1)]
  for dr, dc in dt:
    nr, nc = r+dr, c+dc
    if is_in_range(nr, nc) and board[nr][nc] != -1:
      # 성공시 반환
      if sol((nr, nc), board, cnt + board[nr][nc], move+1):
        board[r][c] = temp # 원상복구
        return True

  board[r][c] = temp  # 원상복구
  return False

board = [list(map(int, input().split())) for _ in range(5)]
r, c = map(int, input().split())

ans = sol((r, c), board, 0, 0)
print(int(ans))


# -----------------------
# 백트래킹 사용 x (내 풀이)
# -1 (장애물)인 칸은 어짜피 이동이 불가해서 백트래킹을 굳이 사용하지 않아도 되는듯함

def is_range_out(r:int, c:int):
  if r > 4 or r < 0:
    return True
  if c > 4 or c < 0:
    return True
  return False
 
def sol(loc:tuple, board:list, cnt:int, move:int):
  if cnt == 2 or move == 3:
    ans.append(cnt)
    return
     
  # 현재 위치
  (r, c) = loc
 
  # 현재 위치 장애물로
  board[r][c] = -1
 
  dt = [[-1, 0], [1, 0], [0, 1], [0, -1]]
 
  for d in dt:
    nxt = (r+d[0], c+d[1])
    if not is_range_out(nxt[0], nxt[1]): # 인덱스 범위 확인
      val = board[nxt[0]][nxt[1]]
      if val != -1: # 이동할 위치가 장애물이 아닐때만 이동
        sol(nxt, board, cnt + val, move+1)
 
board = [list(map(int, input().split())) for _ in range(5)]
r, c = map(int, input().split())
 
ans = []
sol((r, c), board, 0, 0)
print(1 if max(ans) >= 2 else 0)