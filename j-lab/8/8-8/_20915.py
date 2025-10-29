import sys
input = sys.stdin.readline

t = int(input())
ans = []
for _ in range(t):
  x = list(map(int, list(input().rstrip())))
  zeros = x.count(0)
  for i in range(len(x)):
    if x[i] == 6:
      x[i] = 9
  x.sort(reverse=True)

  # 0 제거
  for _ in range(zeros):
    x.pop()

  if len(x) == 0:
    ans.append(str(0))
    continue

  a = x[0]; b = 0
  # 현재 값이 더 작은 쪽에 수를 넣어서 균형 맞추기
  for i in range(1, len(x)):
    if a <= b:
      a = a * 10 +  x[i]
    else:
      b = b * 10 + x[i]
  ans.append(str(a*b*(10**zeros)))

print("\n".join(ans))