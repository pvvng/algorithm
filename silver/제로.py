k = int(input())
stk = []
for _ in range(k):
  x = int(input())
  if(x == 0):
    stk.pop()
    continue
  stk.append(x)

print(sum(stk))