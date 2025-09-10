import sys
input = sys.stdin.readline

# 적어도 M미터의 나무를 집에 가져가기 위해서 절단기에 설정할 수 있는 높이의 최댓값
def sol(A, m):
  A.sort()

  low = 0 # 최소 0미터는 자름
  high = A[-1] # 가장 긴 나무 길이
  ans = -1
  
  while low <= high:
    # mid = h
    h = (low + high) // 2

    # 자를 길이
    # 이게 m과 최대로 비슷하면 됨 (대신 m보다 커야함)
    cuts = sum(max(0, a - h) for a in A)
    # cuts가 m보다 크거나 같은 경우(최댓값을 구하는거니까) -> 더 적게 잘라본다 -> h 늘리기
    if cuts >= m:
      ans = h
      low = h + 1
    # cuts가 m보다 작은 경우 -> 더 많이 잘라야한다 -> h 줄이기
    else:
      high = h - 1

  return ans

n, m = map(int, input().split())
A = list(map(int, input().split()))
print(sol(A, m))