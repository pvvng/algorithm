n = int(input())

for i in range(n):
  print(" " * i + "*" * (2*(n-i)-1))
for j in range(n, 2*n-1):
  print(" " * (2*n-2 - j) + "*" * (-2*n + 2*j + 3))