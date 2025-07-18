def sol(A:str):
  B = ""
  for char in A:
    # using ascii
    # if 97 <= ord(char) <= 122:
    #   B += char
    # using method
    if char.islower():
      B += char
  return B

print(sol(input()))