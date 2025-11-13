import sys
input = sys.stdin.readline

def sol(n, k, no):
  ### D[i]의 의미
  # D[i] = i를 외친 시점에서 현재 차례인 학생이 이길 수 있으면 1, 아니면 0
  # 즉, i를 외쳤다고 가정했을 때,
  # 다음 학생이 부를 수 있는 숫자들(i+1 ~ i+k) 중
  # “패배 상태”로 가는 선택지가 하나라도 있으면 현재 학생은 승리할 수 있다.

  ### 왜 i부터 시작해서 i+k-1까지 보나?
  # i는 “이전 사람이 i-1을 외쳤다”고 가정한 상태다.
  # 즉, 현재 사람이 부를 수 있는 숫자는 i ~ i+k-1 

  ### 그 안에서 j를 선택했을 때 무슨 일이 일어남?
	# 현재 사람이 j를 외친다.
	# 그러면 다음 사람은 j+1부터 시작해서 부르게 된다.
	# 즉, 다음 상태는 D[j+1].

  D = [0] * (n+2)
  for i in range(n, 0, -1):
    # 이전 학생이 i-1를 외쳤을 때 
    # 현재 학생이 i ~ i+k-1 (j) 범주를 외칠 수 있음
    # 각 j에 대해 j+1이 승리인지, 패배인지 확인하면 된다. 
    for j in range(i, i+k):
      if j > n:
        break
      if j in no:
        continue
      # j를 외쳤을 때 다음 학생(j+1)이 패배하면 D[j] = 1
      if D[j+1] == 0:
        D[i] = 1
        break

  return D[1]

n, k = map(int, input().split())
no = set(map(int, input().split()))
print(sol(n, k, no))