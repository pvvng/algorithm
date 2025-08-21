vowel = set(["A","E","I","O","U","a","e","i","o","u"])
for _ in range(int(input())):
  v = 0
  c = 0
  text = input()
  for char in text:
    if char == " ":
      continue
    if char in vowel:
      v += 1
    else:
      c += 1
  print(c, v)