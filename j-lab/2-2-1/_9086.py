def sol(txt:str):
  return txt[0] + txt[-1]

T = int(input())

for _ in range(T):
  print(sol(input()))
