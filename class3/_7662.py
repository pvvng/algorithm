import heapq
import sys
input = sys.stdin.readline

class PriorityQueue:
  def __init__(self):
    self.mxh = []          # (-num, id)
    self.mnh = []          # (num, id)
    self.deads = [False] * 1000000

  def push(self, num, id):
    heapq.heappush(self.mxh, (-num, id))
    heapq.heappush(self.mnh, (num, id))

  def clean(self, sign=1):
    target = self.mxh if sign == 1 else self.mnh
    while target:
      _, id = target[0]
      if not self.deads[id]:
        break
      heapq.heappop(target)

  def pop(self, sign=1):
    target = self.mxh if sign == 1 else self.mnh
    self.clean(sign)
    if not target:
      return None
    num, id = heapq.heappop(target)
    self.deads[id] = True
    return -num if sign == 1 else num
  
ans = []
t = int(input())

for _ in range(t):
  n = int(input())
  pq = PriorityQueue()

  for id in range(n):
    c, num = input().split()
    num = int(num)
    if c == "I":
      pq.push(num, id)
    else:
      pq.pop(num)

  pq.clean(1)
  pq.clean(-1)

  if not pq.mxh or not pq.mnh:
    ans.append("EMPTY")
  else:
    ans.append(f"{-pq.mxh[0][0]} {pq.mnh[0][0]}")

print("\n".join(ans))