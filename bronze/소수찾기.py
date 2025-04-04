import math

n = int(input())
ls = map(int, input().split())
p = []

for v in ls:
  isPrime = True
  for i in range(2, int(math.sqrt(v))+1):
    if(v%i==0) : isPrime = False
  if(isPrime and v != 1) : p.append(v)

print(len(p))