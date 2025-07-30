P = int(input())
C = int(input())

ans = 0
if P > C:
  ans += 500
ans += P * 50
ans -= C * 10

print(ans)