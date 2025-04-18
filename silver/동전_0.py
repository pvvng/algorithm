import sys
input = sys.stdin.readline

n, k = map(int, input().split())

coins = []
for _ in range(n):
  coin = int(input())
  if coin <= k:
    coins.append(coin)

cnt = 0
while k > 0:
  x = coins.pop()
  if x > k:
    continue
  cnt += k // x
  k %= x

print(cnt)