import sys
input = sys.stdin.readline

def get_time_num(t: str):
  hh, mm, ss = map(int, t.split(":"))
  return hh * 60 * 60 + mm * 60 + ss

MAX_TIME = get_time_num("23:59:59") + 1

def sol(A: list):
  diff = [0] * MAX_TIME
  query_2 = []
  for q, start, end in A:
    if q == "1":
      start_time = get_time_num(start)
      end_time = get_time_num(end)
      diff[start_time] += 1
      diff[end_time] -= 1
    else:
      query_2.append((get_time_num(start), get_time_num(end)))

  # 구간 합
  for i in range(1, MAX_TIME):
    diff[i] += diff[i-1]
  
  # 누적 합
  for i in range(1, MAX_TIME):
    diff[i] += diff[i-1]

  # (end - 1) - (start - 1) 
  ans = []
  for start, end in query_2:
    res = diff[end-1]
    if start > 0:
      res -= diff[start - 1]
    ans.append(str(res))

  return "\n".join(ans)

A = [input().split() for _ in range(int(input()))]
print(sol(A))