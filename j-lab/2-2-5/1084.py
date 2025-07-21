# h,m으로 split해서 m 초과값 h로 넘기기
def sol(A: list):
  total_h = 0
  total_m = 0
  for date in A:
    h, m = map(int, date.split(":"))
    total_h += h
    total_m += m
  if total_m >= 60:
    total_h += total_m // 60
    total_m = total_m % 60
  return f"{str(total_h).rjust(2, '0')}:{str(total_m).rjust(2, '0')}"

# 분 단위로 해체해서 h, m 계산
def parse_log(t: str):
  h, m = map(int, t.split(":"))
  return h * 60 + m

def sol2(A:list):
  total = 0
  for d in A:
    total += parse_log(d)
  
  h = total // 60
  m = total % 60

  return f"{str(h).zfill(2)}:{str(m).zfill(2)}"

A = input().split()
print(sol(A))
print(sol2(A))
