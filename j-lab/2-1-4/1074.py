# n, k를 인자로 넣어 리스트로 처리하는 방법
def sol(n:int, k:int):
  cnt = 0
  for _ in range(n):
    lst = list(map(int, input().split()))
    cnt += lst.count(k)
  return cnt

# matrix를 인자로 넣어 2중 배열로 처리하는 방법
def sol2(n:int, matrix:list, k:int):
  cnt = 0
  for i in range(n):
    for j in range(n):
      if matrix[i][j] == k:
        cnt += 1
  return cnt

n, k = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(n)]
print(sol2(n, matrix, k))