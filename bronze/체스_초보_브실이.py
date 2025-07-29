board = [list(input()) for _ in range(8)]
score = { "k": 0, "p": 1, "n": 3, "b": 3, "r": 5, "q": 9 }

black = 0
white = 0

for row in board:
  for e in row:
    if e == ".":
      continue
    s = score[e.lower()]
    if e.isupper():
      white += s
    else:
      black += s

print(white - black)