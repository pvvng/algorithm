class AbsHeap:
  def __init__(self):
    self.arr = []
  
  def push(self, num):
    self.arr.append((abs(num), num))
    current_idx = len(self.arr) - 1

    while current_idx > 0:
      parent_idx = (current_idx-1) // 2
      cur = self.arr[current_idx]
      par = self.arr[parent_idx]

      if cur > par:
        break

      self.__swap__(current_idx, parent_idx)
      current_idx = parent_idx

  def pop(self):
    if len(self.arr) == 0:
      return 0
    
    first = self.arr[0]
    last = self.arr.pop()

    if len(self.arr) == 0:
      return last[1]

    self.arr[0] = last

    length = len(self.arr)
    current_idx = 0
    while True:
      child_idx1 = 2 * current_idx + 1
      child_idx2 = 2 * current_idx + 2

      # 두 child가 모두 없는 경우 
      if child_idx1 >= length:
        break

      # child1은 존재, child2는 없는 경우
      if child_idx1 < length and child_idx2 >= length:
        child_idx = child_idx1
      else:
        if self.arr[child_idx1] < self.arr[child_idx2]:
          child_idx = child_idx1
        else:
          child_idx = child_idx2

      child = self.arr[child_idx]
      cur = self.arr[current_idx]

      if cur < child:
        break

      self.__swap__(child_idx, current_idx)
      current_idx = child_idx

    return first[1]

  def __swap__(self, c, t):
    temp = self.arr[c]
    self.arr[c] = self.arr[t]
    self.arr[t] = temp


import sys
input = sys.stdin.readline

absheap = AbsHeap()
ans = []
for _ in range(int(input())):
  x = int(input())
  if x != 0:
    absheap.push(x)
  else:
    ans.append(str(absheap.pop()))

print("\n".join(ans))