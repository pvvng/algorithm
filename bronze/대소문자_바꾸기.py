txt = input()
ans = ""
for i in range(len(txt)):
  ords = ord(txt[i])
  if ords >= 65 and ords <= 90:
    ans += txt[i].lower()
  else:
    ans += txt[i].upper()
print(ans)