import sys
input = sys.stdin.readline

def sol(n, A, T):
  psum = [0] * n
  psum[0] = A[0]
  for i in range(1, n):
    psum[i] += psum[i-1] + A[i]
  for i, j in T:
    if i == 1:
      print(psum[j-1])
    else:
      print(psum[j-1] - psum[i-2]) 

n = int(input())
A = list(map(int, input().split()))
T = [list(map(int, input().split())) for _ in range(int(input()))]
sol(n, A, T)