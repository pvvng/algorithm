cnt = 0

while True:
  try:
    text = input()
    cnt += 1
  except EOFError:
    break
print(cnt)
