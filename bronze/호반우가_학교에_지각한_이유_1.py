s, d, i, l, n = map(int, input().split())
target = n * 4
cur = s + d + i + l
ans = 0
while cur < target:
  ans += 1
  cur += 1
print(ans)
  
  