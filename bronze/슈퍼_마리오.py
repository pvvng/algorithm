A = [0] * 10
for i in range(10):
  A[i] = A[i-1] + int(input())
miny = float("inf")
ans = -1
for i in range(10):
  if miny >= abs(100 - A[i]):
    miny = abs(100 - A[i])
    ans = A[i]
print(ans)
