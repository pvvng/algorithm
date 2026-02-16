s = []
m = []
for i in range(6):
  if i < 4:
    s.append(int(input()))
  else:
    m.append(int(input()))

s.sort()
m.sort()

print(sum(s[1:]) + m[1])