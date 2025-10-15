import sys
input = sys.stdin.readline

# 일반 요금으로 시간당 1000원
# 야간 정액을 끊으면 5000원만 내고 밤 10시부터 다음날 아침 8시
def sol(T):
  ans = []
  for time, remain in T:
    hh, mm = map(int, time.split(":"))
    hh = (hh + 2) % 24 # 시간에 2를 더해 0시 ~ 10시까지가 야간 범위가 되도록 설정

    remain = int(remain)
    fee = 0
    while remain > 0:
      # 0시 ~ 5시 사이에 300분 이상의 remain이 남아있는 경우에만 정액권 사용
      if hh < 5 and remain >= 5 * 60:
        fee += 5000
        remain -= 10 * 60 - (hh * 60 + mm)
        hh = 10
        mm = 0
      # 1시간 이용
      else:
        hh = (hh + 1) % 24
        remain -= 60
        fee += 1000
    ans.append(str(fee))
    
  return "\n".join(ans)

n = int(input())
T = [input().split() for _ in range(n)]
print(sol(T))