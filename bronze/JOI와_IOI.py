txt = input()

JOI = IOI = 0
idx = 0
while len(txt) > idx:
  t = txt[idx: idx + 3]  
  idx += 1
  if len(t) != 3:
    continue
  if t == "JOI":
    JOI += 1
  elif t == "IOI":
    IOI += 1
print(JOI)
print(IOI)
