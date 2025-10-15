import sys
input = sys.stdin.readline

def get_min_time(s: str):
  m, s = map(int, s.split(":"))
  return m * 60 + s

def get_day_time(start, end):
  day_start = 7 * 60 # 420
  day_end   = 19 * 60 # 1140
  return max(0, min(end, day_end) - max(start, day_start))

def sol(T):
  ofs = 24 * 60 # 1440

  ans = 0
  for hm, dd in T:
    start = get_min_time(hm)
    end_raw = start + int(dd)

    day_time = 0
    # 통화가 자정을 넘음: 두 조각으로 나눔 [start, ofs) + [0, end_raw-ofs)
    if end_raw > ofs:
      # 첫 조각
      day_time += get_day_time(start, ofs)
      # 두번째 조각 (다음날 0부터)
      day_time += get_day_time(0, end_raw - ofs)
    else:
      # 통화 기간 중에서 주간 구간 [7:00, 19:00)에 
      # 겹치는 구간이 몇분인지(길이가 얼마인지) 알아야 한다
      # 겹치는 구간의 길이 구하기 (최솟값 0)
      day_time = get_day_time(start, end_raw)
    # 통화 중 주간 시간 * 10 + (총 통화 지속 시간 - 통화 중 주간 시간) * 5
    ans += day_time * 10 + (int(dd) - day_time) * 5
  return ans

n = int(input())
T = [input().split() for _ in range(n)]
print(sol(T))