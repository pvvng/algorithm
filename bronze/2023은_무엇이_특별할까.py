ans = []
for _ in range(int(input())):
  cur = input()
  nxt = int(int(cur) + 1)
  if nxt % int(cur[-2:]) == 0:
    ans.append("Good")
  else:
    ans.append("Bye")
print("\n".join(ans))
