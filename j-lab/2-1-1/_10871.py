def sol(A:list[int], len:int, target:int) -> list[int]:
  ans = []
  for i in range(len):
    if target > A[i]:
      ans.append(A[i])
  return ans

n, x = map(int, input().split())
A = list(map(int, input().split()))

print(" ".join(map(str, sol(A, n, x))))

# OR use filter method
AS = list(filter(lambda e : e < x, A))
print(" ".join(map(str, AS)))
