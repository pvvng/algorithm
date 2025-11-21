# Max Heap: 부모 노드가 항상 자식 노드보다 크거나 같다

# 배열에 자연수 x를 넣는다.
# 배열에서 가장 큰 값을 출력하고, 그 값을 배열에서 제거한다.

import sys
input = sys.stdin.readline

class MaxHeap:
  def __init__(self):
    self.q = []
  
  def push(self, num):
    self.q.append(num)

    c = len(self.q) - 1

    while c > 0:
      p = (c-1) // 2
      if self.q[c] <= self.q[p]:
        break
      self.__swap__(p, c)
      c = p
    return self.q
  
  def pop(self):
    if len(self.q) == 0:
      return 0
    
    el = self.q[0]
    last = self.q.pop()

    if len(self.q) == 0:
      return last

    # 마지막 노드 맨 위로
    self.q[0] = last
    p = 0

    while True:
      left = 2*p+1
      right = 2*p+2
      bigger_child = p

      # 왼쪽 자식 존재하고 더 크면 교체 후보
      if left < len(self.q) and self.q[left] > self.q[bigger_child]:
        bigger_child = left
      # 오른쪽 자식 존재하고 더 크면 교체 후보
      if right < len(self.q) and self.q[right] > self.q[bigger_child]:
        bigger_child = right

      if bigger_child == p:  # 더 이상 교체할 필요 없으면 종료
        break

      self.__swap__(p, bigger_child)
      p = bigger_child

    return el
  
  def __swap__(self, p_idx, c_idx):
    temp = self.q[p_idx]
    self.q[p_idx] = self.q[c_idx]
    self.q[c_idx] = temp

hq = MaxHeap()
ans = []
for _ in range(int(input())):
  x = int(input())
  if x != 0:
    hq.push(x)
  else:
    ans.append(str(hq.pop()))

print("\n".join(ans))
