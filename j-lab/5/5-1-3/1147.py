def do_add_query(psum, i, j, k):
  psum[i] += k
  if j + 1 < len(psum):
    psum[j + 1] -= k

def sol(T: list, A: list, n: int):
  psum = [0] * n
  Apsum = [0] * n
  flag = False
  for t in T:
    if t[0] == 1:
      do_add_query(psum, t[1], t[2], t[3])
    else:
      if not flag:
        # 누적합
        for i in range(1, n):
          psum[i] += psum[i-1]
        # 누적합 통합
        for i in range(n):
          A[i] += psum[i]
        # A 누적합
        Apsum[0] = A[0]
        for i in range(1, n):
          Apsum[i] += A[i] + Apsum[i - 1]
        flag = True
      if t[1] == 0:
        print(Apsum[t[2]])
      else:
        print(Apsum[t[2]] - Apsum[t[1] - 1])

n, m = map(int, input().split())
A = list(map(int, input().split()))
T = [list(map(int, input().split())) for _ in range(m)]
sol(T, A, n)