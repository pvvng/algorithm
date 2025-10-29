def perm(iter: list):
  n = len(iter)
  res = []
  path = []
  visited = [False] * n

  def dfs():
    if len(path) == n:
      res.append(path[:])
      return 
    
    for i in range(n):
      if visited[i]:
        continue
      # 중복 스킵
      if i > 0 and iter[i] == iter[i-1] and not visited[i-1]:
        continue
      visited[i] = True
      path.append(iter[i])
      dfs()
      path.pop()
      visited[i] = False

  dfs()
  return res

def sol(n, A, op):
  shapes = ["+", "-", "*", "/"]
  ops = []
  for i in range(4):
    for _ in range(op[i]):
      ops.append(shapes[i])
  
  all_ops = (perm(ops))

  res = []
  for op in all_ops:
    prev = 0
    for i in range(n-1):
      if i == 0:
        prev = A[i]
      if op[i] == "+":
        prev += A[i+1]
      elif op[i] == "-":
        prev -= A[i+1]
      elif op[i] == "*":
        prev *= A[i+1]
      elif op[i] == "/":
        if prev >= 0:
          prev //= A[i+1]
        else:
          prev = -((-prev) // A[i+1])
    res.append(prev)


  res.sort()
  return "\n".join(map(str, [res[-1], res[0]]))

n = int(input())
A = list(map(int, input().split()))
op = list(map(int, input().split()))
print(sol(n, A, op))