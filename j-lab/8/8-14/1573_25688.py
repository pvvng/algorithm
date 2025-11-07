import sys
input = sys.stdin.readline

def in_range(r, c):
  return 0 <= r < 5 and 0 <= c < 5

def build_state(prev: str, new: int):
  if new == 0 or new == -1:
    return prev

  new_state = "x"
  for i in range(1, 7):
    if i == new:
      new_state += "1"
    else:
      new_state += prev[i]
  return new_state

def check_state(state: str):
  res = 0
  for i in range(1, 7):
    if state[i] == "1":
      res += 1

  return res == 6

def sol(A:list, loc: tuple):
  idx = 0
  # set에 저장되는 값은 (위치, 현재 상태)이다.
  # 만약 같은 위치이지만 현재 상태가 다르면 방문한걸로 치지 않게되어 
  # 상태에 따라 visited 처리가 가능해짐
  visited = [[set() for _ in range(5)] for _ in range(5)]
  q = [(loc, "x000000", 0)]

  dt = [(0, -1), (0, 1), (1, 0), (-1, 0)]

  while idx < len(q):
    cur, state, move = q[idx]
    if check_state(state):
      return move

    idx += 1
    for nr, nc in dt:
      nr += cur[0]; nc += cur[1]
      if in_range(nr, nc) and (nr, nc, state) not in visited[nr][nc] and A[nr][nc] != -1:
        nxt_state = build_state(state, A[nr][nc])
        visited[nr][nc].add((nr, nc, nxt_state))
        q.append(((nr, nc), nxt_state, move + 1))
      
  return -1

A = [list(map(int, input().split())) for _ in range(5)]
loc = tuple(map(int, input().split()))
print(sol(A, loc))
