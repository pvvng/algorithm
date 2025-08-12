def sol(P:int, S:set)->int:
  ans = 0
  for _ in range(P):
    s = int(input())
    if s in S:
      S.remove(s)
    else:
      ans += 1
  return ans

K = int(input())
for _ in range(K):
  P, M = map(int, input().split())
  S = set(i for i in range(1, M+1))
  print(sol(P, S))
