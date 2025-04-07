from collections import deque

n = int(input())
dq = deque()

for i in range(n):
  dq.append(i + 1)

cnt = 0
while len(dq) != 1:
  fv = dq.popleft()
  if cnt % 2 == 1:
    dq.append(fv)
  cnt += 1

print(dq[0])