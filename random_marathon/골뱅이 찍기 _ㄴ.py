n = int(input())

def golbang(x):
  for _ in range(x):
    print("@", end="")
  print()

for i in range(5):
  for j in range(n):
    golbang(n * (1 if i < 4 else 5))
