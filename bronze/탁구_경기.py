d = p = 0
for _ in range(int(input())):
  winner = input()
  if abs(d - p) >= 2:
    continue
  if winner == "D":
    d += 1
  else:
    p += 1
    
print(f"{d}:{p}")
