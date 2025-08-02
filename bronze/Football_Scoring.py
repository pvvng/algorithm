dt = [6, 3, 2, 1, 2]

for _ in range(2):
  A = list(map(int, input().split()))
  cnt = 0
  for i in range(5):
    cnt += A[i] * dt[i]
  print(cnt)