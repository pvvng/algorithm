import sys
input = sys.stdin.readline

ans = []
while True:
  t = input()
  if t.rstrip() == "-1":
    break
  lst = list(map(int, t.split()))[:-1]
  st = set(lst)

  cnt = 0
  for e in lst:
    if e * 2 in st:
      cnt += 1

  ans.append(cnt)

print("\n".join(map(str, ans)))
