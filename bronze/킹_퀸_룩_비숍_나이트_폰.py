# 킹 1개, 퀸 1개, 룩 2개, 비숍 2개, 나이트 2개, 폰 8개
# 킹, 퀸, 룩, 비숍, 나이트, 폰
ls1 = [1, 1, 2, 2, 2, 8]
ls2 = list(map(int, input().split()))

for i in range(6):
  print(ls1[i] - ls2[i], end=' ')
print()
