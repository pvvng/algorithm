import sys
input = sys.stdin.readline

# (0, 1) => (2, 3) => (4, 5) => (6, 7) => (8, 9) => (10, 11)

### dfs로 풀이 (내 풀이)
def dfs(A, k):
  if k > 11:
    return 0
  
  # k -> sender 전달비용
  sender = k+1 if k % 2 == 0 else k-1
  ans = A[k][sender]

  # 현재 지점이 마지막인 경우 그룹끼리의 전달 비용만 넘기기
  if sender >= 10:
    return ans
  
  # k가 짝수일 때 n1, n2 = k+2, k+2+1
  # k가 홀수일 때 n1, n2 = k+2, k+2-1
  n1 = k+2
  n2 = k+2+1 if k % 2 == 0 else k+2-1

  # sender -> receiver 전달
  # reciver가 n1인 경우
  cost1 = A[sender][n1] + dfs(A, n1)
  # reciver가 n2인 경우
  cost2 = A[sender][n2] + dfs(A, n2)

  # 다음 그룹으로 패스
  return ans + min(cost1, cost2)

### dp를 이용한 풀이(책)
def sol(A):
  # D[i][0]: 친구 집단 i+1 내에서 두번째 친구가 첫번째 친구에게 메시지를 전달하는 최소 시간
  # 그룹 i 내부 전달까지 끝났을 때, 메시지가 그룹 i의 첫 번째 친구(2*i) 에 있는 경우의 최소 누적 시간

  # D[i][1]: 친구 집단 i+1 내에서 첫번째 친구가 두번째 친구에게 메시지를 전달하는 최소 시간
  D = list([0] * 2 for _ in range(6))

  # D[0][0]: 두번째 친구가 첫번째 친구에서 메시지 전달하는 시간(A[0][1])
  # D[0][0]: 첫번째 친구가 두번째 친구에서 메시지 전달하는 시간(A[1][0])
  # A[i][j] == A[j][i] (문제 제한 2. 학생 i가 학생 j에게 메시지를 전달하는 데 걸리는 시간과 학생 j가 학생 i에게 메시지를 전달하는 데 걸리는 시간은 같다.)
  D[0][0] = D[0][1] = A[0][1]

  for i in range(1, 6):
    # 1: 친구 집단 i의 첫번째 친구가 i+1의 두번째 친구에게 메시지 전달
    # 2: 친구 집단 i의 두번째 친구가 i+1의 두번째 친구에게 메시지 전달
    D[i][0] = min(D[i-1][0] + A[2*i-2][2*i+1] + A[2*i][2*i+1], \
                  D[i-1][1] + A[2*i-1][2*i+1] + A[2*i][2*i+1])
    
    # 1: 친구 집단 i의 첫번째 친구가 i+1의 첫번째 친구에게 메시지 전달
    # 2: 친구 집단 i의 두번째 친구가 i+1의 첫번째 친구에게 메시지 전달
    D[i][1] = min(D[i-1][0] + A[2*i-2][2*i] + A[2*i][2*i+1], \
                  D[i-1][1] + A[2*i-1][2*i] + A[2*i][2*i+1])
  
  return min(D[5][0], D[5][1])

A = [list(map(int, input().split())) for _ in range(12)]
print(sol(A))