s = set()
for _ in range(5):
  e = int(input())
  if e in s:
    s.remove(e)
  else:
    s.add(e)
print(s.pop())