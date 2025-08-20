from itertools import permutations

def sol(A: str, B:str):
  S = set()
  for a in permutations(A):
    S.add("".join(a))

  ans = 1
  A = sorted(list(S))
  for i in range(len(A)):
    if A[i] == B:
      ans = i+1
  return ans

A, B = map(str, input().split())
print(sol(A, B))

