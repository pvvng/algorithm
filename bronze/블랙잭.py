# M을 넘지 않으면서 M과 최대한 가깝게

n, m = map(int, input().split())
ls = list(map(int, input().split()))

ans = []

for i in range(n - 2):
  for ii in range(i+1, n - 1):
    for iii in range (ii + 1, n):
      cand = ls[i] + ls[ii] + ls[iii]
      if(m - cand >= 0):
        ans.append(cand)

print(max(ans))