def sol(n:int, A:list):
  d = dict()
  mx = 0
  for i in range(n):
    d.setdefault(A[i], 0)
    d[A[i]] += 1
    mx = max(d[A[i]], mx)

  ans = []
  for key, val in d.items():
    if val == mx:
      ans.append(key)
  
  return sorted(ans)
  
n = int(input())
A = list(map(int, input().split()))
print(*sol(n, A))
