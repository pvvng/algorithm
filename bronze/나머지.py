DIVISON = 42

ls = set()
for _ in range(10):
  ls.add(int(input()) % DIVISON)

print(len(ls))