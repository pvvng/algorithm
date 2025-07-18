def sol(R:int, S:str):
  P = ""
  for char in S:
    P += char * R
  return P

for _ in range(int(input())):
  R, S = input().split()
  print(sol(int(R), S))
  