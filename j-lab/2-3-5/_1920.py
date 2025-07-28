def sol(A, B):
  s = set()
  for a in A:
    s.add(a)
  for b in B:
    print(int(b in s))

N = input()
A = input().split()
M = input()
B = input().split()

sol(A, B)
