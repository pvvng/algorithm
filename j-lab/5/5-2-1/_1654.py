import sys
input = sys.stdin.readline

def sol(N:int, L:list[int]):
  L.sort()

  low = 1
  high = L[-1]

  ans = 0
  # 마지막 후보(=low=high)까지 검사하기 위해 <= 처리
  while low <= high:
    mid = (low + high) // 2
    total = sum(v // mid for v in L)
    # total 길이로 N개 이상 자를 수 있을 때
    # -> 더 길게 도전 (low를 mid까지 업)
    if total >= N:
      ans = mid
      low = mid + 1
    # 너무 크게 자른 경우 -> high를 낮힌다
    # 또한 해당 mid는 불가능한 값이기에 경계에 포함하지 않아야함
    # 따라서 high는 mid - 1
    else:
      high = mid - 1
  
  return ans

K, N = map(int, input().split())
L = [int(input()) for _ in range(K)]
print(sol(N, L))