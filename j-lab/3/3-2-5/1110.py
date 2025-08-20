from itertools import permutations

def sol(A: str):
  S = set()
  for a in permutations(A):
    S.add("".join(a))

  return sorted(list(S))

A, k = map(str, input().split())
k = int(k)

ans = sol(A)
print(ans[k - 1])
