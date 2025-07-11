ls = list(map(int, input().split()))

# solv 1
print(sum(ls))

# solv 2
ans = 0
for e in ls:
  ans += e
print(ans)