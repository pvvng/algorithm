import sys
input = sys.stdin.readline

n, m = map(int, input().split())

pokedex_num = {}
pokedex_str = {}

for i in range(1, n + 1):
  x = input()
  pokedex_num.setdefault(i, x.strip())
  pokedex_str.setdefault(x.strip(), i)

for _ in range(m):
  x = input().strip()
  if x.isdigit():
    print(pokedex_num.get(int(x)))
  else:
    print(pokedex_str.get(x))
