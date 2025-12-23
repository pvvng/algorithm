# 마지막에 올 수 있는 블록은
# |, =, ㅁ
# | 블록의 경우에 n-1 블록의 개수와 같음
# =, ㅁ 블록의 경우에 n-2의 개수와 같음
# 즉, 점화식은 f(n) = 2 * f(n-2) + f(n-1)

def sol(n):
  if n == 1: return 1
  if n == 2: return 3
  p1 = 1; p2 = 3
  for _ in range(3, n+1):
    temp = p1
    p1 = p2
    p2 = 2 * temp + p2

  return p2 % 10007

print(sol(int(input())))