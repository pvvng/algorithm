# set
# x, y = map(int, input().split())
# A = set(input().split())
# B = set(input().split())
# print(len(A-B) + len(B-A))

# set2
def sol(x, A, y, B):
  SA = set()
  for i in range(x):
    SA.add(A[i])
  SB = set()
  for i in range(y):
    SB.add(B[i])
  ans = 0
  for e in SA:
    if e not in SB:
      ans += 1
  for e in SB:
    if e not in SA:
      ans += 1
  return ans
          
x, y = map(int, input().split())
A = input().split()
B = input().split()
print(sol(x, A, y, B))