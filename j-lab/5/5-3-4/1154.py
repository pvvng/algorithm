import math
# 기본 시간(분): 100분, 기본 요금(원): 10, 단위 시간(분): 50, 단위 요금(원): 3
# 통화 요금은 학생별로 통화 시간에 대하여 청구된다. 
# 통화 시간이 기본 시간 이하라면 기본 요금이 청구된다. 
# 통화 시간이 기본 시간을 초과하면, 기본 요금에 더해서, 초과한 시간에 대해서 단위 시간마다 단위 요금이 청구된다. 
# 초과한 시간이 단위 시간으로 나누어 떨어지지 않으면 올림 한다.
def get_min(t: str):
  mm, ss = t.split(":")
  mm = int(mm); ss = int(ss)
  return mm * 60 + ss

def sol(T: list):
  ans = 0
  for t in T:
    if get_min(t) <= 100:
      ans += 10
    else:
      exceed = math.ceil((get_min(t) - 100) / 50)
      ans += 10 + exceed * 3
  return ans

T = input().split()
print(sol(T))