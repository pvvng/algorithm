n = int(input())
k = int(input())

ans = n
for i in range(1, k+1):
  ans += int(str(n) + ("0" * i))
print(ans)