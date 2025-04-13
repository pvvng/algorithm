# 아직 아무 의견이 없다면 문제의 난이도는 0으로 결정한다.
# 의견이 하나 이상 있다면, 문제의 난이도는 모든 사람의 난이도 의견의 30% 절사평균으로 결정한다.

# 30% 절사평균의 경우 위에서 15%, 아래에서 15%를 각각 제외하고 평균을 계산한다. 
# 따라서 20명이 투표했다면, 가장 높은 난이도에 투표한 3명과 가장 낮은 난이도에 투표한 3명의 투표는 평균 계산에 반영하지 않는다는 것이다.
# 제외되는 사람의 수는 위, 아래에서 각각 반올림한다. 25명이 투표한 경우 위, 아래에서 각각 3.75명을 제외해야 하는데, 이 경우 반올림해 4명씩을 제외한다.
# 마지막으로, 계산된 평균도 정수로 반올림된다. 절사평균이 16.7이었다면 최종 난이도는 17이 된다.

import sys
input = sys.stdin.readline

def round(x:int) -> int:
  if x - int(x) >= 0.5:
    return int(x) + 1
  return int(x)

n = int(input())

if n <= 0:
  print(0)
else:
  ls = [int(input()) for _ in range(n)]
  ofs = round(n * 15 / 100)
  sliced_ls = sorted(ls)[ofs:n-ofs]
  print(round(sum(sliced_ls)/len(sliced_ls)))