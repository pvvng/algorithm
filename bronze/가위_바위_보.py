def RSP(p1, p2):
  if p1 == p2:
    return (0, 0)
  if p1 == "R" and p2 == "S" or \
    p1 == "S" and p2 == "P" or \
    p1 == "P" and p2 == "R":
    return (1, 0)
  return (0, 1)

ans = []
for _ in range(int(input())):
  player = [0, 0]
  for _ in range(int(input())):
    a, b = input().split()
    res = RSP(a, b)
    player[0] += res[0]
    player[1] += res[1]
  if player[0] > player[1]:
    ans.append("Player 1")
  elif player[0] < player[1]:
    ans.append("Player 2")
  else:
    ans.append("TIE")
print("\n".join(ans))
