N = int(input())
files = list(map(int, input().split()))
size = int(input())

ans = 0
for file in files:
  ans += file // size
  ans += 1 if file % size > 0 else 0

print(ans * size)