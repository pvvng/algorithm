import sys
input = sys.stdin.readline

A = 0; B = 0
for _ in range(int(input())):
  x, y = map(int, input().split())
  if x > y : A+=1
  elif x < y : B+=1
print(A, B)