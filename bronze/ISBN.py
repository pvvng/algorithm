isbn = list(input())
l = isbn[0::2] # *1
r = isbn[1::2] # *3
trg = sm = 0
for idx in range(len(isbn)):
  d = (1 if idx % 2 == 0 else 3)
  if isbn[idx] == "*":
    trg = d
    continue
  sm += d * int(isbn[idx])

for x in range(10):
  if (sm + x * trg) % 10 == 0:
    print(x)
    break