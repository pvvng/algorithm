def search(target:int, A:list, n: int):
  if A[0] > target:
    return n
  if A[-1] <= target:
    return 0
  
  low = 0
  high = n - 1
  while low < high:
    mid = (low + high) // 2
    # mid 가 target보다 크면 실패지점까지 high = mid
    if target < A[mid]:
      high = mid
    # mid 가 target보다 작거나 같으면 mid를 포함한 좌측엔 정답이 존재하지 않는다.
    else:
      low = mid + 1
  return n - high

def sol(n, A, T):
  A.sort()
  ans = []
  for t in T:
    ans.append(search(t, A, n))
  return ans

n, m = map(int, input().split())
A = list(map(int, input().split()))
T = [int(input()) for _ in range(m)]
for e in sol(n, A, T):
  print(e)
