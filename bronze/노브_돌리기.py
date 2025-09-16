def sol(A:list[int], initial:int):
  current = initial
  ans = 0
  for target in A:
    if target >= current:
      ans += min(target - current, 360 - target + current)
    else:
      ans += min(current - target, 360 - current + target)
    current = target
  return ans

n = int(input())
A0 = int(input())
A = list(int(input()) for _ in range(n))
print(sol(A, A0))