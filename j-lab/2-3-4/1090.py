# 왜 이렇게 하는지 모르겠음. 너무 비효율적인데
def sol(A, B):
  D = {}
  for phone in A:
    for i in range(len(phone) - 1):
      x = phone[:i+1]
      print(D)
      if x in D:
        D[x] += 1
      else:
        D[x] = 1

  if B in D:
    return D[B]
  else:
    return B

A = input().split()
B = input()

print(sol(A, B))

# 문제 해결엔 이게 맞지않나?
def my_sol(A, B):
  cnt = 0
  for e in A:
    if e.startswith(B) and e != B:
      cnt += 1
  return cnt

print(my_sol(A, B))