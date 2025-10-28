# 현재 학생이 이기는 경우가 있으면 최대한 빨리 끝내기
# 현재 학생이 이기는 경우가 없으면 최대한 늦게 끝내기
def sol(n, k, A):
  no = [False] * (n+1)
  no[0] = True
  for a in A:
    no[a] = True

  return abs(dfs(n, k, 0, no))

def dfs(n, k, a, no):
  # 기저 조건: a가 n이면 더 이상 외칠 수 없으므로 현재 플레이어는 패배
  if n == a:
    return 0  # 0은 '더 이상 진행 불가' 상태
  
  # 다음에 부를 수 있는 후보 숫자 목록
  nxt = []
  for i in range(a+1, a+k+1):
    if i > n:
      break
    if no[i]:
      continue
    nxt.append(dfs(n, k, i, no))

  # 다음에 부를 수 있는 숫자가 하나도 없으면 현재 플레이어는 패배
  if len(nxt) == 0:
    return 0
  
  nxt.sort()

  # nxt 리스트에는 “다음 상태의 결과값”이 들어있는데,
  # 이 값의 부호로 승패를 표현함:
  #   - 양수 -> 상대가 이기는 경우 (즉, 현재는 지는 상황)
  #   - 음수 -> 상대가 지는 경우 (즉, 현재는 이기는 상황)
  # 절댓값은 “앞으로 남은 총 턴 수”를 의미함

  # (이 코드에서는 nxt[0] > 0이면 -> 모든 값이 양수 -> 이길 수 없음)
  if nxt[0] > 0:
    # 이길 수 있는 경우가 없다면, 어차피 질 거니까 최대한 늦게 지기
    # 가장 큰 값(즉, 가장 오래 버티는 경우)에 +1 턴 추가 후 음수로 표시
    # +1 을 더하는건 현재 학생이 외친 정수를 가산한 것
    return -(nxt[-1] + 1)

  # 이길 수 있는 경우가 있다면(즉, nxt 안에 음수 값이 존재) -> 가능한 한 빨리 끝내기
  # 즉, nxt 중 음수(상대가 지는 경우) 중 절댓값이 가장 작은 것을 선택
  ret = None
  for i in range(len(nxt)):
    if nxt[i] <= 0: # 상대가 지는 경우만 탐색
      ret = nxt[i]
  # ret은 음수이므로 (-ret + 1)은 '현재는 이기고 앞으로 남은 턴 수 +1'
  return -ret + 1
    
n, k = map(int, input().split())
A = list(map(int, input().split()))
print(sol(n, k, A))