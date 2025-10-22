import sys
input = sys.stdin.readline

# 문자열 조합 구하는 함수
def comb(string, k):
  res = set()
  path = []
  def dfs(start):
    if len(path) == k:
      res.add("".join(path))
      return
    for i in range(start, len(string)):
      path.append(string[i])
      dfs(i + 1)
      path.pop()

  dfs(0)
  return res

# 두 번 이상 나타나는 부분 문자열 구하는 함수
def get_intersection(X: set, Y: set, Z: set):
  res = set()
  for x in X:
    if x in Y or x in Z:
      res.add(x)
  for y in Y:
    if y in X or y in Z:
      res.add(y)
  for z in Z:
    if z in Y or z in X:
      res.add(z)
  return res

def sol(x, y, z, k):
  res = get_intersection(comb(x, k), comb(y, k), comb(z, k))
  if len(res) == 0:
    return -1
  return sorted(res)

x = input().strip()
y = input().strip()
z = input().strip()
k = int(input())

ans = sol(x, y, z, k)
if ans != -1:
  print("\n".join(ans))
else:
  print(ans)