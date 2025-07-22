# my sol
def init(n: int)->dict:
  A = dict()
  for _ in range(n):
    name, price = map(str, input().split())
    price = int(price)
    A[name] = price
  return A
  
def sol(A:dict, m:int, B:list):
  ans = 0
  for i in range(m):
    ans += A[B[i]]
  return ans

n, m = map(int, input().split())
A = init(n)
B = input().split()
print(sol(A, m, B))

# 한번에 하는 풀이
def sol2(A, B):
  products = dict()
  for (name, cost) in A:
    products[name] = int(cost)

  ans = 0
  for e in B:
    ans += products[e]
  return ans

n, m = map(int, input().split())
A1 = [tuple(input().split()) for _ in range(n)]
B1 = input().split()
print(sol2(A1, B1))