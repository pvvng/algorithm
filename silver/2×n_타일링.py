MAX = 1000
factorial = [1] * (MAX + 1)
for i in range(1, MAX + 1):
  factorial[i] = factorial[i - 1] * i

def combination (n, m):
  return factorial[n + m] // (factorial[n] * factorial[m])

n = int(input())
tc = n // 2

res = 1
for i in range(1, tc + 1):
  res += combination(i, n - i * 2)

print(res % 10007)