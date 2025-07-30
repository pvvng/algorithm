# 차집합
# A = set(input().split())
# B = set(input().split())
# ans = sorted(list(A - B))

# for i in ans:
#   print(i)

# set
def sol(A:list, B:list):
  S = set(B)
  ans = []
  for a in A:
    if a not in S:
      ans.append(a)
  return sorted(ans)

A = input().split()
B = input().split()
for e in sol(A, B):
  print(e)