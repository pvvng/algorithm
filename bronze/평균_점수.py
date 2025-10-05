ans = 0
for _ in range(5):
  x = int(input())
  ans += 40 if x < 40 else x
print(ans // 5)