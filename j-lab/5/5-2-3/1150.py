# 배열 A의 원소 중 i보다 크거나 같고 j보다 작거나 같은 원소의 개수를 출력한다.

# target 좌측에 있는 원소 개수 구하기
def search_low(target, A):
  n = len(A)
  res = 0
  low = 0
  high = n - 1
  while low <= high:
    mid = (low + high) // 2
    if A[mid] <= target:
      res = mid
      low = mid + 1
    else:
      high = mid - 1
  return n - res - 1

# target 우측에 있는 원소 개수 구하기
def search_high(target, A):
  n = len(A)
  res = n
  low = 0
  high = n - 1
  while low <= high:
    mid = (low + high) // 2
    if target <= A[mid]:
      res = mid
      high = mid - 1
    else: 
      low = mid + 1
  return n - res

def sol(A, T):
  A.sort()
  ans = []
  for i, j in T:
    ans.append(max(0, search_high(i, A) - search_low(j, A)))
  return ans

n, m = map(int, input().split())
A = list(map(int, input().split()))
T = [list(map(int, input().split())) for _ in range(m)]
for e in sol(A, T):
  print(e)