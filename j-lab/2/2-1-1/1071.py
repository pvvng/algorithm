def count(n :int, A :list, k :int):
  ans = 0
  for i in range(n):
    if k == A[i]:
      ans += 1
  return ans

n, k = map(int, input().split())
A = list(map(int, input().split()))

print(count(n, A, k))

# OR use count method
print(A.count(k))