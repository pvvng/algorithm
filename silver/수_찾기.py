n = int(input())
ls = set(map(int, input().split()))
m = int(input())
ck = list(map(int, input().split()))

for i in ck:
  print(int(i in ls))