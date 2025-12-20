n = int(input())
ans = 0
note = "-1"
for i in range(1, n+1):
  ans += 1
  if "50" in note:
    ans += 1
  note = str(i)

print(ans)