import sys
input = sys.stdin.readline

def get_time_num(t: str):
  hh, mm, ss = map(int, t.split(":"))
  return hh * 60 * 60 + mm * 60 + ss

MAX_TIME = get_time_num("23:59:59") + 1

def sol(A: list):
  ans = 0
  diff = [0] * (MAX_TIME + 1)

  for a in A:
    if a[0] == "1":
      ss = get_time_num(a[1])
      ee = get_time_num(a[2])
      diff[ss] += 1
      if ee < MAX_TIME:
        diff[ee] -= 1
    else:
      L = get_time_num(a[1])
      # 구간 합
      for i in range(1, MAX_TIME):
        diff[i] += diff[i-1]
      # 누적합
      for i in range(1, MAX_TIME):
        diff[i] += diff[i-1]

      # 시작을 최댓값으로 지정 
      ans = diff[L-1]
      # 가능한 범위 [i:start ~ i+L:end]
      for i in range(1, MAX_TIME-L+1):
        ret = diff[i+L-1] - diff[i-1]
        if ans < ret:
          ans = ret
  return ans

A = [input().split() for _ in range(int(input()))]
print(sol(A))