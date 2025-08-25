# 조합 vs 순열

# - 순열(permutation): 순서가 중요
  # 예) (5,6,7) 과 (6,5,7)은 다른 경우로 침
  # for i in range(start, n) 식으로 인덱스를 점점 뒤로 미루면서 탐색

# - 조합(combination): 순서가 중요하지 않음 
  # 예) (5,6,7) 과 (6,5,7)은 같은 경우로 침
  # visited로 관리

def sol(start: int, cnt: int, total: int):
  global best # 함수 안에서 전역 변수(함수 밖에 있는 변수)를 직접 수정
  if cnt == 3:
    best = max(total, best)
    return

  for i in range(start, n):
    if total + cards[i] <= m:
      sol(i + 1, cnt + 1, total + cards[i])

n, m = map(int, input().split())
cards = list(map(int, input().split()))
best = 0
sol(0, 0, 0)
print(best)
