# 백준(선공)은 한 번에 최대 9배로 키울 수 있으니, “내가 한 번에 이길 수 있는 범위”는 p ≥ ceil(n/9) 이상일 때다(9를 곱하면 ≥ n).
# 반대로 동혁(후공)은 백준이 이기는 걸 막으려면 가능한 한 작게 만들려 할 것이다 
# — 즉, 후공은 일반적으로 최소 배수(=2) 를 골라서 다음 상황을 불리하게 만들려고 한다.
def sol(n):
  x = 1
  turn = 0

  while True:
    if turn == 0:
      x *= 9
    else:
      x *= 2

    if x >= n:
      break

    turn = (turn + 1) % 2

  return "Baekjoon" if turn % 2 == 0 else "Donghyuk"

ans = []

while True:
  try:
    ans.append(f"{sol(int(input()))} wins.")
  except EOFError:
    break

print("\n".join(ans))
