txt = input()
ans = txt.split("(")
if len(ans) > 1:
  ans[1] = ans[1][:-1]
ans[0] = ans[0].strip()
for i in range(2):
  if i == 1 and len(ans) == 1:
    print("-")
    break
  print(ans[i])