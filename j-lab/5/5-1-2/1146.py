def sol(n:int, A:list, B: list):
  psum = [0] * n

  for b in B:
    if b[0] == 1:
      do_add_query(psum, b[1], b[2], b[3])
    else:
      for i in range(1, n):
        psum[i] += psum[i-1]
      return sum(psum[b[1]:b[2] + 1]) + sum(A[b[1]: b[2] + 1])

def do_add_query(psum, i, j, k):
  psum[i] += k
  if j < n-1:
    psum[j+1] -= k

n, m = map(int, input().split())
A = list(map(int, input().split()))
B = [list(map(int, input().split())) for _ in range(m)]
print(sol(n, A, B))