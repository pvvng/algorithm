def sol(S:str)->str:
  new_s = ""
  prev = ""

  for char in S:
    is_continous = False
    t = char.lower()

    if prev == t:
      is_continous = True

    if is_continous:
      new_s = new_s[:len(new_s) - 1] + new_s[-1].lower()
    else:
      new_s += char

    prev = t

  return new_s

S = input()
print(sol(S))