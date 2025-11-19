import sys
input = sys.stdin.readline

def sol(n, k, no):
  # D[i]는 i ~ i+k-1 범주에서의 정답 
  # 이길 수 있으면 최솟값
  # 이길 수 없으면 최댓값 * - 1
  D = [0] * (n+2)

  for i in range(n, 0, -1):
    nxt = []
    # 이전 학생이 i-1을 외쳤다
    # 현재 학생이 i ~ i+k-1 범위에서 외친다
    for j in range(i, i+k):
      if j > n:
        break
      if j in no:
        continue

      # 현재 학생이 외친 값인 j에 대한 다음 값인 j+1 확인
      nxt.append(D[j+1])

      if len(nxt) == 0:
        D[i] = 0
        continue

      nxt.sort()

      # 현재 학생이 지는 경우 = 최솟값도 양수
      # 이길 수 없으니 최댓값을 저장
      if nxt[0] > 0:
        D[i] = -(nxt[-1] + 1)
        continue

      # 현재 학생이 이길 수 있는 경우 = 최솟값이 양수가 아님
      # nxt 배열의 음수 중 최솟값 저장
      ret = None
      for p in range(len(nxt)):
        if nxt[p] <= 0:
          ret = nxt[p]

      D[i] = -ret + 1
  
  return abs(D[1])

n, k = map(int, input().split())
no = set(map(int, input().split()))
print(sol(n, k, no))