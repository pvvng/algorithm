n = int(input())


for i in range(n):
  blank = n - i - 1
  star = i + 1
  print(" " * blank + "*" * star)