# 각 숫자 사이에는 1cm의 여백이 들어가야한다.
# 1은 2cm의 너비를 차지해야한다. 0은 4cm의 너비를 차지해야한다. 나머지 숫자는 모두 3cm의 너비를 차지한다.
# 호수판의 경계와 숫자 사이에는 1cm의 여백이 들어가야한다.

while True:
  x = list(input())
  ans = len(x) + 1
  if x[0] == "0" and len(x) == 1:
    break
  for e in x:
    if e == "1":
      ans += 2
    elif e == "0":
      ans += 4
    else:
      ans += 3
  print(ans)
