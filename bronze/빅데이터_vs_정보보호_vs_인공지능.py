n = list(input())
txt = input()
counts = {
  "B": 0,
  "S": 0,
  "A": 0,
}
for c in txt:
  counts[c] += 1
maxy = 1
ans = ""
for key in counts:
  if counts[key] > maxy:
    maxy = counts[key]
    ans = key   
  elif counts[key] == maxy:
    ans += key
if len(ans) == 3:
  ans = "SCU"
print(ans)