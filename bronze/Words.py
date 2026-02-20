import sys
input = sys.stdin.readline

ans = []
while True:
  txt = input().split()
  if len(txt) == 1 and txt[0] == "#":
    break
  rev = []
  for s in txt:
    rv = ""
    for c in s:
      rv = c + rv 
    rev.append(rv)
  ans.append(" ".join(rev))

print("\n".join(ans))
  