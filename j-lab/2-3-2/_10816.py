
def sol(N:int, target:list, M:int, checks:list):
  haves = dict()
  for i in range(N):
    card = target[i]
    haves.setdefault(card, 0)
    haves[card] += 1
  ans = []
  for ii in range(M):
    check = checks[ii]
    val = haves.get(check)
    if not val:
      val = 0
    ans.append(val)
  return ans

N = int(input())
target = input().split()
M = int(input())
checks = input().split()
ans = sol(N, target, M, checks)
print(*ans)
