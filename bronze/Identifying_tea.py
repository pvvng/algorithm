T = int(input())
ls = list(map(int, input().split()))
cnt = 0
for e in ls:
  if e == T:
    cnt += 1
print(cnt)