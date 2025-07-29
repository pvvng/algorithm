from collections import deque

N, K = map(int, input().split())
deq = deque()
ans = []

for i in range(1, N + 1):
  deq.append(i)

while len(deq) > 0:
  deq.rotate(-(K-1))
  ans.append(deq.popleft())

print("<" + ", ".join(map(str, ans)) + ">")