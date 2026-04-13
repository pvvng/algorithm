ans = []
for _ in range(int(input())):
  txt = input()
  ret = "Do-it"
  if txt[len(txt) // 2 - 1] != txt[len(txt) // 2]:
    ret += "-Not"
  ans.append(ret)

print("\n".join(ans))