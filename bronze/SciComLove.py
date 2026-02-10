l = "SciComLove"

txt = input()
cnt = 0

for i in range(len(txt)):
  if txt[i] != l[i]:
    cnt += 1

print(cnt)