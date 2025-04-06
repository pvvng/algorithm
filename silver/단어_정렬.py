words = set()

n = int(input())

for _ in range(n):
  w = input()
  words.add((w, len(w)))

words = list(words)
words.sort(key=lambda x : (x[1], x[0]))

for v in list(map(lambda x : x[0], words)):
  print(v)