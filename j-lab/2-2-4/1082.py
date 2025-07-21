# using set
def sol(A:str, B:set):
  C = ""
  for char in A:
    if char in B:
      char = char.lower()
    C += char
  return C

A = input()
B = set(input().split())

print(sol(A, B))

# using replace method
def sol2(A:str, B:list):
  for char in B:
    # replace(target, change)
    A = A.replace(char, char.lower())
  return A

A = input()
B = input().split()

print(sol2(A, B))