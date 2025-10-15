# 기본 시간(분): 100분, 기본 요금(원): 10, 단위 시간(분): 50, 단위 요금(원): 3

# 누적 통화 시간이 기본 시간 이하라면 기본 요금이 청구
# 누적 통화 시간이 기본 시간을 초과하면, 
# 기본 요금에 더해서 초과한 시간에 대해서 단위 시간마다 단위 요금이 청구
# 초과한 시간이 단위 시간으로 나누어떨어지지 않으면 올림

# 통화 요금이 같은 학생은 학생 이름 기준으로 오름차순으로 출력

import sys
input = sys.stdin.readline

BASIC = (100, 10)
UNIT = (50, 3)

def get_min_time(s: str):
  h, m = map(int, s.split(":"))
  return h * 60 + m

def sol(T):
  d = {}
  res = []
  for time, name in T:
    d.setdefault(name, 0)
    d[name] += get_min_time(time)
  for key in d:
    check = d[key] - BASIC[0]
    fee = BASIC[1]
    etc = 0
    if check > 0:
      etc += (check // UNIT[0]) * UNIT[1]
      etc += UNIT[1] if check % UNIT[0] else 0
    res.append((key, fee + etc))

  res.sort(key=lambda x : (-x[1], x[0]))
  ans = []
  for name, fee in res:
    ans.append(f"{name} {fee}")
  return "\n".join(ans)

n = int(input())
T = [input().split() for _ in range(n)]
print(sol(T))
