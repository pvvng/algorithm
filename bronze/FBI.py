ans = []
for i in range(1, 6):
  name = input()
  if "FBI" in name:
    ans.append(i)

if len(ans) == 0:
  print("HE GOT AWAY!")
else:
  print(*ans)