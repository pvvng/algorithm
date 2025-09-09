def sol(n:int, A:list, T:list):
  A.sort()

  ans = []
  for k in T:
    # 배열의 모든 원소가 k보다 크거나 같은 경우
    if A[0] >= k:
      ans.append(n)
      continue
    # 배열의 모든 원소가 k보다 작은 경우
    elif A[-1] < k:
      ans.append(0)
      continue
    # k <= A[i]를 만족하는 가장 작은 i를 찾는다.
    # A[i-1] < k <= A[i]
    # k <= A[i...n-1]인 값을 찾는다.
    low = 0
    high = n - 1
    while low < high:
      mid = (low + high) // 2

      # k가 A[mid]의 왼쪽에 있는 경우 왼쪽을 추가 탐색한다.
      if k <= A[mid]:
        high = mid
      else: # k가 A[mid]의 오른쪽 부분에 있는 경우 오른쪽을 추가 탐색한다.
        low = mid + 1
    ans.append(n - high)
  return ans

n, m = map(int, input().split())
A = list(map(int, input().split()))
T = [int(input()) for _ in range(m)]
for e in sol(n, A, T):
  print(e)
