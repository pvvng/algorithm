n = int(input())
ls = list(map(int, input().split()))

ans = 0
for e in ls:
  ans += min(e, n) 
print(ans)