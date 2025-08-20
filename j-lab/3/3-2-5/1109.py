from itertools import permutations

def sol(A: str):
  S = set()
  for a in permutations(A):
    S.add("".join(a))

  return sorted(list(S))

A = input()
ans = sol(A)
for e in ans:
  print(e)
