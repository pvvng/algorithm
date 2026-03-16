def sol(cur: str):
  oa = ord("A")
  return chr(oa + ((ord(cur) + 1 - oa) % 26))

ans = []
for _ in range(int(input())):
  loop, cur = input().split()
  loop = int(loop)
  ret = []
  for i in range(loop):
    ret.append(cur * (i+1))
    cur = sol(cur)
  ans.append("\n".join(ret))
print("\n\n".join(ans))
