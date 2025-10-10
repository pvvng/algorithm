a, b, n, w = map(int, input().split())
ans = "-1"
for i in range(1, n):
  if a * i + b * (n - i) == w:
    if ans != "-1": # 가능한 해가 두개 이상인 경우
      ans = "-1"
      break
    ans = f"{i} {n - i}"

print(ans)