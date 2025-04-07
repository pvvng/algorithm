# push X: 정수 X를 스택에 넣는 연산이다.
# pop: 스택에서 가장 위에 있는 정수를 빼고, 그 수를 출력한다. 만약 스택에 들어있는 정수가 없는 경우에는 -1을 출력한다.
# size: 스택에 들어있는 정수의 개수를 출력한다.
# empty: 스택이 비어있으면 1, 아니면 0을 출력한다.
# top: 스택의 가장 위에 있는 정수를 출력한다. 만약 스택에 들어있는 정수가 없는 경우에는 -1을 출력한다.

class stack:
  def __init__(self):
    self.st = []

  def _isEmpty(self):
    return len(self.st) == 0

  def push(self, x):
    self.st.append(x)

  def pop(self):
    if self._isEmpty():
      return -1
    return self.st.pop()
  
  def size(self):
    return len(self.st)

  def empty(self):
    if self._isEmpty():
      return 1
    return 0

  def top(self):
    if self._isEmpty():
      return -1
    return self.st[-1]

n = int(input())
stk = stack()
prt = []

for _ in range(n):
  work = input()
  if "push" in work:
    pv = int(work.split()[1])
    stk.push(pv)
  if work == "pop":
    prt.append(stk.pop())
  if work == "size":
    prt.append(stk.size())
  if work == "empty":
    prt.append(stk.empty())
  if work == "top":
    prt.append(stk.top())

for i in prt:
  print(i)