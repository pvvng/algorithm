def sol(A:str, B:list):
  for char in B:
    A = A.replace(char, char.upper())
  return A

A = input()
B = input().split()
print(sol(A, B))