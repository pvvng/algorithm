def sol(txt: str):
  idx = [-1] * 26
  for i in range(26):
    char = chr(i + 97)
    if idx[i] == -1:
      idx[i] = txt.find(char)
  return idx

for i in sol(input()):
  print(i, end=" ")
