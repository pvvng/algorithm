cnt = 0
ans = []
while True:
  cnt += 1
  txt = input()
  if txt == "Was it a cat I saw?":
    break
  new_txt = ""
  for i in range(0, len(txt), cnt + 1):
    new_txt += txt[i]
  ans.append(new_txt)
print("\n".join(ans))
