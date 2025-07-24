def sale(c: int, p: int):
  ans = []
  if c >= 5:
    ans.append(max(p - 500, 0))
  if c >= 10:
    ans.append(p * 90 // 100)
  if c >= 15:
    ans.append(max(p - 2000, 0))
  if c >= 20:
    ans.append(p * 75 // 100)
  ans.append(p)
  return min(ans)

c = int(input())
p = int(input())
print(sale(c, p))
