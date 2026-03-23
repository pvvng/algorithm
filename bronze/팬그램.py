ans = []
while True:
  txt = input()
  if txt == "*":
    break
  a = set()
  for c in txt:
    if c == " ":
      continue
    a.add(c)
  ans.append("Y" if len(a) == 26 else "N")
print("\n".join(ans))
