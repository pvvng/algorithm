def sol(txt:str):
  return txt[0].upper() + (txt[1:])

for _ in range(int(input())):
  print(sol(input()))