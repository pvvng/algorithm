# 배(0)와 등(1)
# 도(배 한 개, 등 세 개), 개(배 두 개, 등 두 개), 걸(배 세 개, 등 한 개), 윷(배 네 개), 모(등 네 개)
# 도는 A, 개는 B, 걸은 C, 윷은 D, 모는 E
def sol(L: list):
  b = 0
  for l in L:
    if l == 0:
      b += 1
  return b + 64 if b > 0 else 69

for _ in range(3):
  L = list(map(int, input().split()))
  print(chr(sol(L)))