from collections import deque

n = int(input())

def ps_to_int(ps: str) -> int:
  if ps == "(":
    return -1
  if ps == ")":
    return 1
  return 0

def say_yes_or_no(isYes : bool):
  if(isYes):
    return "YES"
  else:
    return "NO"

res = []

for _ in range(n):
  lq = deque()
  rq = deque(input())
  flag = True
  while len(rq) != 0:
    r_pv = rq.popleft()
    r_psi = ps_to_int(r_pv)
    # 얼리 리턴
    if(len(lq) == 0 and r_psi == 1):
      flag = False
      break
    if(len(lq) != 0):
      l_psi = ps_to_int(lq[-1])
      # 성공
      if (l_psi + r_psi == 0):
        lq.pop()
        continue
    lq.append(r_pv)

  if len(lq) != 0 :
    flag = False

  res.append(say_yes_or_no(flag))

for i in res:
  print(i)
