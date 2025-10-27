import sys
input = sys.stdin.readline

# iter에서 k 이하의 가능한 조합의 합을 찾는 함수
def comb(iter, k) -> set:
  res = set()
  path = []

  def dfs(start):
    if len(path) > k:
      return

    if len(path) > 0:
      res.add(sum(list(path)))
    
    for i in range(start, len(iter)):
      path.append(iter[i])
      dfs(i + 1)
      path.pop()

  dfs(0)
  return res

n = int(input())
A = list(map(int, input().split()))
print(sum(A) - len(comb(A, n)))