import sys

S = sys.stdin.readline().rstrip()
q = int(sys.stdin.readline())

count = [[0] * 26] # 길이 0일 때(아무 문자도 안 본 상태) 누적 카운트 = 모두 0
for i in range(len(S)):
  count.append(count[len(count) - 1][:]) # 직전 누적을 '복사'해서 한 줄 추가
  count[i + 1][ord(S[i]) - 97] += 1  # 현재 문자 1 증가

for _ in range(q):
  a, l, r = map(str, sys.stdin.readline().split())
  result = count[int(r) + 1][ord(a) - 97] - count[int(l)][ord(a) - 97]
  print(result)