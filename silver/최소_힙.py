import sys
input = sys.stdin.readline

class min_heap():
  def __init__(self):
    self.hq = []

  def get(self):
    return self.hq
  
  def append(self, num:int):
    self.hq.append(num)
    self.__bubble_up(len(self.hq) - 1)

  def pop(self):
    # 빈 힙에 pop 요청시 0 반환
    if len(self.hq) == 0:
      return 0
    # 마지막 요소 최상단 요소와 교환후 마지막 요소 제거
    pop_element = self.__swap_root_with_top_element()
    # 탑다운 정렬
    self.__shift_down(0)

    return pop_element
  
  def __bubble_up(self, idx: int):
    # idx가 0 이하면 변경할 부모가 존재하지 않음
    while idx > 0:
      parent_idx = self.__get_parent_idx(idx)
      # 부모가 변경할 자식보다 작아 변경한 이유가 없을때 break
      if not self.__check_change_idx(idx, parent_idx):
          break
      self.__swap(idx, parent_idx)
      idx = parent_idx

  def __swap_root_with_top_element(self) :
    self.__swap(0, len(self.hq) - 1)
    return self.hq.pop()
  
  def __shift_down(self, idx:int):
    while True:
      # 변경할 자식이 존재하지 않으면 break
      child_idx = self.__get_smaller_child_idx(idx)
      if child_idx is None or self.hq[idx] <= self.hq[child_idx]:
        break
      self.__swap(idx, child_idx)
      idx = child_idx

  def __get_smaller_child_idx(self, parent_idx:int):
    left_idx = parent_idx * 2 + 1
    right_idx = parent_idx * 2 + 2

    candidates = []
    if left_idx < len(self.hq):
      candidates.append(left_idx)
    if right_idx < len(self.hq):
      candidates.append(right_idx)

    # 자식이 존재하지 않는 리프 노드일때 None 반환
    if not candidates:
      return None
    
    # 자식 노드 중 최소값 반환
    return min(candidates, key=lambda idx: self.hq[idx])
  
  def __get_parent_idx(self, child_idx:int):
    return 0 if child_idx == 0 else (child_idx - 1) // 2

  def __swap(self, change_idx: int, target_idx:int):
    temp = self.hq[target_idx]
    self.hq[target_idx] = self.hq[change_idx]
    self.hq[change_idx] = temp

  def __check_change_idx(self, child_idx: int, parent_idx: int) -> bool:
    return self.hq[parent_idx] > self.hq[child_idx]

n = int(input())
hq = min_heap()

res = []
for _ in range(n):
  x = int(input())
  if bool(x):
    hq.append(x)
  else:
    print(hq.pop())