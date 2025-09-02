# def in_range(r, c):
#   return 0 <= r <= 4 and 0 <= c <= 4

# def sol(loc: tuple, apple_num: int, move: int, cand: list):
#   if apple_num == 3:
#     cand.append(move) 
#     return
  
#   (r, c) = loc
#   temp = board[r][c]
#   board[r][c] = -1

#   dt = [(0, 1), (0, -1), (1, 0), (-1, 0)]
#   for dr, dc in dt:
#     nr, nc = dr+r, dc+c
#     if in_range(nr, nc) and board[nr][nc] != -1:
#       sol((nr, nc), apple_num + max(0, board[nr][nc]), move + 1, cand)
  
#   board[r][c] = temp

# board = [list(map(int, input().split())) for _ in range(5)]
# r, c = map(int, input().split())
# cand = []
# sol((r, c), 0, 0, cand)
# if len(cand) > 0:
#   print(min(cand))
# else:
#   print(-1)

def in_range(r, c):
  return 0 <= r <= 4 and 0 <= c <= 4

def sol(board:list, aloc:list):
  return solve(board, aloc, 3)
  
def solve(board:list, aloc:list, apple_num:int):
  # 사과를 모두 먹은 경우 추가 이동 필요없음
  if apple_num == 0:
    return 0
  
  # 현재 위치에서 apple_num개 사과를 먹기 위한 최소 이동 횟수
  ret = -1
  dd = [[-1, 0], [1, 0], [0, -1], [0, 1]]
  for dr, dc in dd:
    # 다음 위치
    r, c = aloc[0] + dr, aloc[1] + dc
    # 이동 가능한 위치일 때
    if in_range(r, c) and board[r][c] != -1:
      prv_value = board[aloc[0]][aloc[1]]
      # 현재 위치 장애물화
      board[aloc[0]][aloc[1]] = -1
      # 다음 위치에 대한 사과 갯수 기록하여 이동
      cur_ret = solve(board, [r, c], apple_num - board[r][c])

      if cur_ret != -1:
        cur_ret += 1
      
      if cur_ret != -1:
        if ret == -1 or cur_ret < ret:
          ret = cur_ret
      
      board[aloc[0]][aloc[1]] = prv_value
  
  return ret

board = [list(map(int, input().split())) for _ in range(5)]
aloc = list(map(int, input().split()))
print(sol(board, aloc))