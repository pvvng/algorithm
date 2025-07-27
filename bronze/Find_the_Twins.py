def sol(a: list):
  ans = []
  if "18" in a:
    ans.append("mack")
  if "17" in a:
    ans.append("zack")

  if len(ans) == 0:
    return "none"
  if len(ans) == 1:
    return ans[0]
  else:
    return "both"

for _ in range(int(input())):
  a = input()
  print(a)
  print(sol(a.split()))
  print()