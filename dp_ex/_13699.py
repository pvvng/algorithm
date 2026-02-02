n = int(input())
t = [1] * (n+1)
for i in range(1, n+1):
  cur = 0
  for j in range(i):
    cur += t[j] * t[i-j-1]
  t[i] = cur
print(t[n])
