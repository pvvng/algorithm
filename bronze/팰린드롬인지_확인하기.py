def sol(txt:str, i:int, j:int):
  if i >= j:
    return 1
  if txt[i] != txt[j]:
    return 0
  return sol(txt, i + 1, j - 1)

txt = input()
print(sol(txt, 0, len(txt) - 1))