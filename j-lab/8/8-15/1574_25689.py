import sys
input = sys.stdin.readline

def in_range(r, c):
  return 0 <= r < 5 and 0 <= c < 5

def check_state(cur: str = "x000000"):
  count = 0
  for c in cur:
    if c == "1":
      count += 1

  return count == 6

def create_state(cur: str = "x000000", idx: int = 0):
  if idx == 0 or idx == 7:
    return cur
  new = "x"
  for i in range(1, len(cur)):
    if i == idx:
      new += "1"
      continue
    new += cur[i]
  return new

def run(A: list, cur: tuple, dir: tuple):
  nxt = (cur[0], cur[1])
  # 1. 장애물, 보드 끝 직전까지 달린다.
  # 2. 7이면 해당 자리에서 정지한다.
  while True:
    nr, nc = nxt[0] + dir[0], nxt[1] + dir[1]
    if not in_range(nr, nc):
      break
    if A[nr][nc] == -1:
      break
    nxt = (nr, nc)
    if A[nr][nc] == 7:
      break
    
  return nxt

def sol(A: list, loc: tuple):
  visited = [[set() for _ in range(5)] for _ in range(5)]

  idx = 0
  q = [(loc[0], loc[1], 0, create_state())]
  dt = [(0, 1), (0, -1), (1, 0), (-1, 0)]

  while idx < len(q):
    cr, cc, move, state = q[idx]

    if check_state(state):
      return move

    idx += 1
    for dr, dc in dt:
      nr = dr + cr
      nc = dc + cc
      # 이동
      if in_range(nr, nc) and state not in visited[nr][nc] and A[nr][nc] != -1:
        val = A[nr][nc]
        nxt_state = create_state(state, val)
        q.append((nr, nc, move + 1, nxt_state))
        visited[nr][nc].add(nxt_state)
      # 달리기
      run_r, run_c = run(A, (cr, cc), (dr, dc))
      if state not in visited[run_r][run_c]:
        val = A[run_r][run_c]
        nxt_state = create_state(state, val)
        q.append((run_r, run_c, move + 1, nxt_state))
        visited[run_r][run_c].add(nxt_state)
    
  return -1

A = [list(map(int, input().split())) for _ in range(5)]
r, c = map(int, input().split())
print(sol(A, (r, c)))