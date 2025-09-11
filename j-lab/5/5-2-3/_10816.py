import sys
input = sys.stdin.readline
# 이진 탐색으로 풀어보기

# 첫번째 target <= A[mid] 구간 찾기
def lower_bound(target:int, A:list[int]):
  low, high = 0, len(A) - 1
  ans = len(A)
  while low <= high:
    mid = (low + high) // 2
    if target <= A[mid]:
      ans = mid
      high = mid - 1
    else:
      low = mid + 1
  return ans

# 첫번재 target < A[mid] 구간 찾기
def higher_bound(target:int, A:list[int]):
  low, high = 0, len(A) - 1
  ans = len(A)
  while low <= high:
    mid = (low + high) // 2
    if target < A[mid]:
      ans = mid
      high = mid - 1
    else:
      low = mid + 1
  return ans

def sol(A:list[int], B:list[int]):
  A.sort()
  ans = []
  for b in B:
    ans.append(str(higher_bound(b, A) - lower_bound(b, A)))
  return ans

N = int(input())
A = list(map(int, input().split()))
M = int(input())
B = list(map(int, input().split()))
ans = sol(A, B)
print(" ".join(ans))
