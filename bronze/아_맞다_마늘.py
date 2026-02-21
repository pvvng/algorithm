n = int(input())
A = set(input().split())
B = set(input().split())

for a in A:
  if a not in B:
    print(a)
    break