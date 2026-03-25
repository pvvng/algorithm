txt = input()
ans = True
for i in range(len(txt) // 2 + 1):
  if txt[i] != txt[-1-i]:
    ans = False    
    break
print("true" if ans else "false")