x = [56, 24, 14, 6]
y = list(map(int, input().split()))
cnt = 0
for i in range(len(x)):
  cnt += x[i] * y[i]
print(cnt)