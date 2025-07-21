def sol(x:str):
  # dict 변환
  dct = dict()
  for char in x.upper():
    dct[char] = dct.get(char, 0) + 1
  lst_kv = list(dct.items())
  mx = max(list(dct.values()))
  ans = list(filter(lambda x: x[1] == mx, lst_kv))
  if len(ans) > 1:
    return "?"
  return ans[0][0]

x = input()
print(sol(x))