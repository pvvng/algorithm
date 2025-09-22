import sys
input = sys.stdin.readline

def q1(n: int, k: int, A: list[int]):
  low = 0; high = n - 1
  while low <= high:
    mid = (low + high) // 2 
    if A[mid] < k:
      low = mid + 1
    else:
      high = mid - 1 
  return n - high - 1

def q2(n: int, k: int, A: list[int]):
  low = 0; high = n - 1
  while low <= high:
    mid = (low + high) // 2 
    if A[mid] <= k:
      low = mid + 1
    else:
      high = mid - 1 
  return n - high - 1

def sol(n:int, A: list[int], T:list[list[int]]):
  A.sort()
  ans = []
  for t in T:
    q = t[0]
    if q == 1:
      k = t[1]
      ans.append(q1(n, k, A))
    elif q == 2:
      k = t[1]
      ans.append(q2(n, k, A))
    else:
      i, j = t[1], t[2]
      ans.append(q1(n, i, A) - q2(n, j, A))
  return ans

n, m = map(int, input().split())
A = list(map(int, input().split()))
T = [list(map(int, input().split())) for _ in range(m)]
ans = sol(n, A, T)
print("\n".join(map(str, ans)))