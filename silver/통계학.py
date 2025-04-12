# 산술평균 : N개의 수들의 합을 N으로 나눈 값
# 중앙값 : N개의 수들을 증가하는 순서로 나열했을 경우 그 중앙에 위치하는 값
# 최빈값 : N개의 수들 중 가장 많이 나타나는 값
# 범위 : N개의 수들 중 최댓값과 최솟값의 차이

# 첫째 줄에는 산술평균을 출력한다. 소수점 이하 첫째 자리에서 반올림한 값을 출력한다.
# 둘째 줄에는 중앙값을 출력한다.
# 셋째 줄에는 최빈값을 출력한다. 여러 개 있을 때에는 최빈값 중 두 번째로 작은 값을 출력한다.
# 넷째 줄에는 범위를 출력한다.

import sys
input = sys.stdin.readline

n = int(input())
ls = [int(input()) for _ in range(n)]

s = 0
frq = {}
sorted_ls = sorted(ls)

for v in sorted_ls:
  s += v
  frq.setdefault(v, 0)
  frq[v] += 1

maxy = max(frq.values())
frq_vals = []
for key in frq:
  if frq[key] == maxy:
    frq_vals.append(key)

print(round(s / n))
print(sorted_ls[n//2])
print(sorted(frq_vals)[1] if len(frq_vals) >= 2 else frq_vals.pop())
print(sorted_ls[n-1] - sorted_ls[0])
