ans = []
for _ in range(int(input())):
  x = input()
  if not x.endswith("."):
    x += "."
  ans.append(x)
print("\n".join(ans))