A = set([int(input()) for _ in range(28)])
ans = []
for i in range(1, 31):
  if i not in A:
    ans.append(i)
for e in sorted(ans):
  print(e)