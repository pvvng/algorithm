n = int(input())
H = list(map(int, input().split()))

cnt = 1
for i in range(n-1):
  if H[i+1] >= H[i]:
    cnt += 1

print(cnt)