def dfs(A: list, pa: int, n: int, ans: set):
  if len(A) == n:
    ans.add(pa)
    return
  
  for i in range(1, 10):
    A.append(i)
    dfs(A, pa * i, n, ans)
    A.pop()

def sol(n: int):
  ans = set()
  dfs([], 1, n, ans)
  return len(ans)

n = int(input())
print(sol(n))