mx = 0
ans = -1

for i in range(9):
  x = int(input())
  if x > mx:
    mx = x
    ans = i + 1

print(mx)
print(ans)
