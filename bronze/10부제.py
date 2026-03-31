n = input()
A = list(map(str, input().split()))
ans = 0
for a in A:
  if a[-1] == n:
    ans += 1
print(ans)
