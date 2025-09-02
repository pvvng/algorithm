def sol(Q: list):
  total_length = get_time("23:59:59") + 1
  B = [0] * total_length

  for query in Q:
    ans = 0
    type, st, et = query
    i = get_time(st); j = get_time(et)
    # 더하기
    if type == "1":
      add_query(B, i, j)
    else:
     ans = get_sum(B, i, j, total_length)

  return ans

def get_time(time: str):
  hh, mm, ss = map(int, time.split(":"))
  return hh * 60 * 60 + mm * 60 + ss

def add_query(B, i, j):
  # 구간 시작에 +1
  B[i] += 1
  # 구간 마지막에 -1 
  # j는 종료구간, 즉 원래 +가 안되는 구간이니까 굳이 j+1로 인덱스 조절할 필요가 없음.
  B[j] -= 1

def get_sum(B, i, j, total_length):
  # 구간합 출력
  for idx in range(1, total_length):
    B[idx] += B[idx - 1]
  return (sum(B[i:j]))

Q = [input().split() for _ in range(int(input()))]
print(sol(Q))