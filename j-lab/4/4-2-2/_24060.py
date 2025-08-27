import sys
sys.setrecursionlimit(10**7)

cnt = 0
answer = -1

def merge_sort(A, p, r):
  global cnt, answer
  if p < r:
    q = (p + r) // 2
    merge_sort(A, p, q)
    merge_sort(A, q + 1, r)
    merge(A, p, q, r)

def merge(A, p, q, r):
  global cnt, answer
  tmp = []
  i, j = p, q + 1

  while i <= q and j <= r:
    if A[i] <= A[j]:
      tmp.append(A[i]); i += 1
    else:
      tmp.append(A[j]); j += 1

  while i <= q:
    tmp.append(A[i]); i += 1
  while j <= r:
    tmp.append(A[j]); j += 1

  # A[p..r]에 다시 저장하며 카운트 체크
  for t, val in enumerate(tmp):
    A[p + t] = val
    cnt += 1
    if cnt == K:
      answer = val

N, K = map(int, input().split())
A = list(map(int, input().split()))

merge_sort(A, 0, N - 1)
print(answer if cnt >= K else -1)