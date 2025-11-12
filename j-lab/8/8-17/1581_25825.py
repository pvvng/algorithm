import sys
input = sys.stdin.readline

def permutation(iter, k):
  res = []
  path = []
  visited = [False] * len(iter)

  def dfs():
    if len(path) == k:
      res.append(tuple(path))
      return

    for i in range(len(iter)):
      if visited[i]:
        continue
      path.append(iter[i])
      visited[i] = True
      dfs()
      path.pop()
      visited[i] = False

  dfs()

  return res

def sol(A):
  ans = float("inf")
  # 순열로 가능한 경로를 모두 조회한다.
  for path in permutation([i for i in range(6)], 6):
    ret = dp(A, path)
    if ans > ret:
      ans = ret
  return ans

def dp(A, path):
  # D[k][0] -> k 그룹의 첫번째 학생이 편지를 가진 상태의 최솟값
  # D[k][1] -> k 그룹의 두번째 학생이 편지를 가진 상태의 최솟값
  D = list([0] * 2 for _ in range(6))

  start = path[0]
  # 시작 지점
  D[0][0] = A[start*2+1][start*2]
  D[0][1] = A[start*2][start*2+1]

  for i in range(1, 6):
    p = path[i-1] # 이전 그룹
    k = path[i] # 현재 그룹
    # k 그룹에서 1>0 전이는 반드시 발생한다.
    # 즉, A[2*k+1][2*k] 는 반드시 존재
    # k-1(p) 그룹에서 2*k+1 학생에게 편지를 전달하는 케이스를 확인
    D[i][0] = min(D[i-1][0] + A[2*p][2*k+1] + A[2*k+1][2*k], \
                  D[i-1][1] + A[2*p+1][2*k+1] + A[2*k+1][2*k])
    
    # k 그룹에서 0>1 전이는 반드시 발생한다.
    # 즉, A[2*k][2*k+1] 는 반드시 존재
    # k-1(p) 그룹에서 2*k 학생에게 편지를 전달하는 케이스를 확인
    D[i][1] = min(D[i-1][0] + A[2*p][2*k] + A[2*k][2*k+1], \
                  D[i-1][1] + A[2*p+1][2*k] + A[2*k][2*k+1])

  return min(D[5][0], D[5][1])

A = [list(map(int, input().split())) for _ in range(12)]
print(sol(A))