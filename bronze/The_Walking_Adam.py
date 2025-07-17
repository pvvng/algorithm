def sol(w: str):
  x = w.split("D")
  return len(x[0])

for _ in range(int(input())):
  print(sol(input()))