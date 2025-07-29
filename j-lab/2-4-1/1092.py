import sys
input = sys.stdin.readline

from collections import deque

ans = (0, 0)
deq = deque()

for i in range(int(input())):
  crt = list(map(int, input().split()))
  if crt[0] == 1:
    deq.append(crt[1])
    if ans[0] < len(deq) or (ans[0] == len(deq) and ans[1] > crt[1]):
      ans = (len(deq), crt[1])
  elif crt[0] == 2:
    deq.popleft()
    
print(ans[0], ans[1])