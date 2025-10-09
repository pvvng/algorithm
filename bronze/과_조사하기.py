# 1, 2반에는 소프트웨어개발과, 3반에는 임베디드소프트웨어개발과, 4반에는 인공지능소프트웨어개발과
ans = [0] * 4
for _ in range(int(input())):
  c, p, _ = map(int, input().split())
  if c == 1:
    ans[3] += 1
  else:
    ans[max(0, p-2)] += 1

for e in ans:
  print(e)
