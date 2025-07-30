def sol(txt:str, size:int=10)->list[str]:
  ln = len(txt)
  lst = []
  for i in range(ln//size + 1):
    lst.append(txt[i*size:(i+1)*size])
  return lst

for e in sol(input()):
  print(e)