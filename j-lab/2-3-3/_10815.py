def sol(cards, M, checks):
  ans = [0] * M
  for i in range(M):
    if checks[i] in cards:
      ans[i] = 1
  return ans

N = int(input())
cards = set(input().split())
M = int(input())
checks = input().split()
print(*sol(cards, M, checks))