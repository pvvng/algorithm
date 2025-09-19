# # 문제 풀이 핵심
# 1. 상태(State)를 어떻게 정의하느냐
# 	•	단순히 (r, c)만으로는 부족해.
# 	•	“문제를 해결하는 데 필요한 맥락(진행도)”까지 상태에 포함해야 돼.
# 	•	이 문제에선 “몇 번까지 밟았는가 = p”가 핵심 맥락.
# → 그래서 (r, c, p)가 진짜 상태였던 거지.

# ➡️ 상태 정의가 잘못되면 BFS/DFS가 길을 다 막아버려서 답이 안 나옴.

# 2. 진행도(progress)를 어떻게 갱신하느냐
# 	•	진행도 p는 오직 p+1인 숫자를 밟았을 때만 +1 된다.
# 	•	다른 칸(0, -1, 이미 지난 숫자 등)은 그냥 지나가거나 무시.
# 	•	즉, 이동 규칙과는 별개로 진행 규칙을 별도로 두는 게 포인트야.

# ➡️ 이걸 “위치 이동”과 “퀘스트 단계 업데이트”를 분리한다고 생각하면 돼.
# (어드벤처 게임에서 열쇠 → 문 순서로 깨야 하는 것과 똑같음.)

def in_range(r, c):
  return 0 <= r <= 4 and 0 <= c <= 4

# i가 적혀 있는 칸에서 i + 1이 적혀 있는 칸으로 이동할 때 다른 번호가 적힌 칸을 방문해도 된다.
def sol(board:list, loc:tuple):
  dt = [(0,1),(0,-1),(1,0),(-1,0)]

  idx = 0
  # r, c, p, d
  queue = [(loc[0], loc[1], 0, 0)]
  visited = [[[False] * 7 for _ in range(5)] for _ in range(5)]
  visited[loc[0]][loc[1]][0] = True
  
  while idx < len(queue):
    r, c, p, dist = queue[idx]

    if p == 6: # found v
      return dist # d
    
    idx += 1
    
    for d in dt:
      nr, nc = r + d[0], c + d[1] # add r, c
      if not in_range(nr, nc):
        continue
      np = p + 1 if board[nr][nc] == p + 1 else p
      if board[nr][nc] != -1 and not visited[nr][nc][np]:
        queue.append((nr, nc, np, dist + 1))
        visited[nr][nc][np] = True
  
  return -1

board = [list(map(int, input().split())) for _ in range(5)]
r, c = map(int, input().split())
print(sol(board, (r, c)))