def recursion(s, l, r):
  global cnt
  cnt += 1
  if s[l] != s[r]:
    return 0
  if l >= r:
    return 1
  else:
    return recursion(s, l+1, r-1)

for i in range(int(input())):
  S = input()
  cnt = 0
  ans = recursion(S, 0, len(S) - 1)
  print(ans, cnt)