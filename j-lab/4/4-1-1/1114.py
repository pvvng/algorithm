# from itertools import combinations

# def sol(A, k:int):
#   comb = list(combinations(A, k))
#   ans = ["".join(c) for c in comb]
#   return sorted(ans)

# A = input().strip()
# k = int(input())
# ans = sol(A, k)
# for a in ans:
#   print(a)

def combination(current:list, visited:set, start:int):
  if len(current) == k:
    ans.append("".join(current))
    return

  for i in range(start, len(A)):
    if i not in visited:
      current.append(A[i])
      visited.add(i)
      combination(current, visited, i + 1)
      current.pop()
      visited.remove(i)
  
A = list(input().strip())
k = int(input())
ans = []
combination([], set(), 0)
for e in sorted(ans):
  print(e)
