# Px = Pn + (x-n+1)
# Px는 현재 IOI형태, Pn은 구할 IOI 형태
# 즉, Pn의 개수 = x-n+1

n = int(input())
m = int(input())
s = input()

ans = 0

i = 0
cnt = 0
# 슬라이딩 윈도우
while i < m:
  cur = s[i]
  if i+1 < m:
    cur += s[i+1]
  if i+2 < m:
    cur += s[i+2]
  # IOI 확인, 연속 검증
  # 윈도우 두 칸 밀기
  if cur == "IOI":
    cnt += 1
    i += 2
  else:
    if cnt:
      ans += max(0, cnt-n+1)
    cnt = 0
    i += 1

print(ans)