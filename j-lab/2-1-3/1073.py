def sol(A:list, B:list) -> int :
  a = b = 0
  for x, y in zip(A, B):
    if x > y:
      a+=1
    elif y > x:
      b+=1
  return int(a > b)

A = list(map(int, input().split()))
B = list(map(int, input().split()))

print(sol(A, B))
