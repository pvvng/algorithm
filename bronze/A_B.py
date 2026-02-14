A, B = map(int, input().split())

# 정수 부분
print(A // B, end='')

# 나머지 있으면 소수점 시작
r = A % B
if r != 0:
  print('.', end='')
  
  for _ in range(1000):  # 충분한 자리수
    r *= 10
    print(r // B, end='')
    r %= B
    if r == 0:
      break