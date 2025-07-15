def sol(n: int, guests: list) -> int:
  rejected = 0
  tables = set()
  for i in range(n):
    if not guests[i] in tables:
      tables.add(guests[i])
      continue
    rejected += 1
  return rejected

n = int(input())
guests = list(map(int, input().split()))

print(sol(n, guests))