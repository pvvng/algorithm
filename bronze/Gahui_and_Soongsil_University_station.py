P = {
  "Es" : 21,
  "Stair" : 17
}

cnt = 0
for _ in range(4):
  t, num = map(str, input().split())
  num = int(num)
  cnt += num * P[t.strip()]

print(cnt)