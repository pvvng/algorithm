from collections import deque

gg = ["[", "]", "(", ")"]
ans = []
while True:
  txt = input()
  if txt == ".":
    break
  stk = []
  que = deque(n for n in list(txt) if n in gg)
  while len(que) != 0:
    qp = que.popleft()
    if len(stk) > 0:
      s = stk[-1] + qp
      if s == "()" or s == "[]":
        stk.pop()
        continue
    stk.append(qp)

  if len(stk) > 0:
    ans.append("no")
  else:
    ans.append("yes")

for v in ans:
  print(v)