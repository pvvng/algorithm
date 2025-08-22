def sol(N:int, M:int, board:list) -> list:
  points = get_points(N, M)
  cands = []

  for point in points:
    (np, mp) = point
    for start_color in ["B", "W"]:
      cnt = 0
      for n in range(np, np + 8):
        for m in range(mp, mp + 8):
          if not is_right_color(n-np, m-mp, board[n][m], start_color):
            cnt += 1
      cands.append(cnt)

  return min(cands)
   
def get_points(N:int, M:int):
  points = []
  for i in range(N - 7):
    for j in range(M - 7):
      points.append((i, j))
  return points

def swap_color(c: str):
  return "W" if c == "B" else "B"

def is_right_color(n:int, m:int, b:str, start:str):
  if (n+m) % 2 == 0 and b == start:
    return True
  if (n+m) % 2 == 1 and b == swap_color(start):
    return True
  return False

N, M = map(int, input().split())
board = [input() for _ in range(N)]
print(sol(N, M, board))