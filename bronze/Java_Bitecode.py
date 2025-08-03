java = set(["J", "A", "V"])

n = int(input())
x = input()

ans = ""
for i in range(n):
  if x[i] not in java:
    ans += x[i]

if ans == "":
  ans = "nojava"

print(ans)