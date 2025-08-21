def combination(start:int, current:list, visited:set, n:int, m:int):
  if len(current) == m:
    print(*current)
    return

  for i in range(start, n + 1):
    if i not in visited:
      current.append(i)
      visited.add(i)
      combination(i + 1, current, visited, n, m)
      current.pop()
      visited.remove(i)

n, m = map(int, input().split())
combination(1, [], set(), n, m)
