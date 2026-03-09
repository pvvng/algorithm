def sol(d, n, D, N):
  # D[i]에 들어갈 수 있는 피자의 최대 지름
  for i in range(1, d):
    D[i] = min(D[i-1], D[i])
  
  # 피자가 들어갈 수 있는 오븐의 최대 깊이
  pos = d-1
  idx = 0
  while pos >= 0:
    # 피자 배치 가능
    if N[idx] <= D[pos]:
      idx += 1
      # 모든 피자 배치 완료
      if idx == n:
        break
    # 다음 오븐 확인
    pos -= 1

  if idx < n:
    return 0
  else:
    return pos + 1

import sys
input = sys.stdin.readline

d, n = map(int, input().split())
D = list(map(int, input().split()))
N = list(map(int, input().split()))
print(sol(d, n, D, N))
