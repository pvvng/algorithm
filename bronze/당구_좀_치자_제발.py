n = int(input())
lst = list(map(int, input().split()))
rage = []
crt = 0
for i in range(n):
  crt += 1 if bool(lst[i]) else -1
  rage.append(crt)
print(sum(rage))