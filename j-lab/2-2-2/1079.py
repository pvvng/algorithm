def sol(A:str):
  B = ""
  for char in A:
    if char.isupper():
      B += char
  return B

print(sol(input()))