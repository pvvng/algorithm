from collections import deque
x = int(input())

for _ in range(x):
  n, m = map(int, input().split())
  ls = list(map(int, input().split()))
  pq = deque((v, ls[v]) for v in range(n))

  index = 0
  while len(pq) > 0:
    pop_element = pq.popleft()
    isExist = bool(len([v for v in pq if v[1] > pop_element[1]]))
    if isExist:
      pq.append(pop_element)
      continue
    index += 1
    if pop_element[0] == m:
      print(index)
      break
