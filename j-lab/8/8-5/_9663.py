import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

# 아이디어 1: 각 행마다 하나의 퀸만 놓을 수 있다. 여러 퀸을 한 행에 놓을 수 없다.
# 아이디어 2: 퀸의 이동경로 (열, 대각선 우측, 대각선 좌측)을 각 visited로 분리해야한다. 
def in_range(n, loc: tuple[int, int]):
  r, c = loc
  return 0 <= r < n and 0 <= c < n

# 보드의 각 열을 순회하면서 착수가 가능한 지점을 찾는다
def dfs(n: int, r:int, visited:list):
  ans = 0

  if r == n:
    return 1
  
  for c in range(n):
    if not visited[0][c] and not visited[1][r+c] and not visited[2][r-c]:
      visited[0][c] = True
      visited[1][r+c] = True
      visited[2][r-c] = True
      ans += dfs(n, r+1, visited)
      visited[0][c] = False
      visited[1][r+c] = False
      visited[2][r-c] = False

  return ans

def sol(n: int):
  # visited 종류를 3가지로 나눌 수 있다.
  # 1. 행
  col_visited = [False] * n
  # 2. ↗️ (row + col: 0 ~ (n-1) + (n-1))
  diag_right_visited = [False] * (2 * n -1)
  # 3. ↖️ (row - col: (-(n-1) ~ +(n-1) ))
  diag_left_visited = [False] * (2 * n -1)

  return dfs(n, 0, [col_visited, diag_right_visited, diag_left_visited])

n = int(input())
print(sol(n))
