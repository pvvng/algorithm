import sys
input = sys.stdin.readline

def sol(p, n, ls):
  start, end = 0, n-1
  state = 0

  for q in p:
    if q == "R":
      start, end, state = R(start, end, state)
    if q == "D":
      ret = D(n, start, end, state)
      # 에러 발생
      if ret == "E":
        return "error"
      start = ret

  d = 1 if state % 2 == 0 else -1

  res = []
  for i in range(start, end + d, d):
    res.append(str(ls[i]))
  
  ans = "[" + ",".join(res) + "]"
  return ans

# start, end 인덱스 포인터 스왑
def R(start, end, state):
  return (end, start, (state + 1) % 2)

# start 포인트 이동으로 pop 대체 
def D(n, start, end, state):
  # 삭제 시점에 이미 비어있으면 에러
  if state % 2 == 0:
    # 정상 방향: 유효 조건은 start <= end
    if start > end:
      return "E"
    return start + 1
  else:
    # 반전 방향: 유효 조건은 start >= end
    if start < end:
      return "E"
    return start - 1

def to_list(ls: str):
  if ls == "[]":
    return []
  return list(map(int, ls[1:len(ls)-1].split(",")))

ans = []
for _ in range(int(input())):
  p = list(input().rstrip())
  n = int(input())
  ls = to_list(input().rstrip())
  ans.append(sol(p, n, ls))
print("\n".join(ans))
