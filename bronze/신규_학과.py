n = int(input())
ans = ""
y = -1
for _ in range(n):
  name, year = input().split()
  if y < int(year):
    ans = name
    y = int(year)
print(ans)
