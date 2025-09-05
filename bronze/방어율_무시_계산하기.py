def sol(A:list[int]):
  V = 0.0
  for a in A:
    V = (1 - (1 - V / 100) * (1 - a / 100)) * 100
    print(V)

N = int(input())
A = list(map(int, input().split()))
sol(A)
