# push X: 정수 X를 큐에 넣는 연산이다.
# pop: 큐에서 가장 앞에 있는 정수를 빼고, 그 수를 출력한다. 만약 큐에 들어있는 정수가 없는 경우에는 -1을 출력한다.
# size: 큐에 들어있는 정수의 개수를 출력한다.
# empty: 큐가 비어있으면 1, 아니면 0을 출력한다.
# front: 큐의 가장 앞에 있는 정수를 출력한다. 만약 큐에 들어있는 정수가 없는 경우에는 -1을 출력한다.
# back: 큐의 가장 뒤에 있는 정수를 출력한다. 만약 큐에 들어있는 정수가 없는 경우에는 -1을 출력한다.

from collections import deque

n = int(input())
dq = deque()
res = []

def isEmpty(dq):
  return len(dq) == 0

for _ in range(n):
  work = input()
  if "push" in work:
    dq.append(int(work.split()[1]))
  if work == "pop":
    if isEmpty(dq):
      res.append(-1)
    else:
      res.append(dq.popleft())
  if work == "size":
    res.append(len(dq))
  if work == "empty":
    res.append(int(isEmpty(dq)))
  if work == "front":
    if isEmpty(dq):
      res.append(-1)
    else:
      res.append(dq[0])
  if work == "back":
    if isEmpty(dq):
      res.append(-1)
    else:
      res.append(dq[-1])

for i in res:
  print(i)