def dfs(current: list, visited: set, n: int, m: int):
  if len(current) == m:
    print(*current)
    return
  
  for i in range(1, n + 1):
    if i not in visited:
      current.append(i)
      visited.add(i)

      dfs(current, visited, n, m)

      current.pop()
      visited.remove(i)

n, m = map(int, input().split())
dfs([], set(), n, m)
