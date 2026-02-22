k = int(input())
txt = input()

ans = ""
idx = 0
while idx < len(txt):
  ans += txt[idx]
  idx += k

print(ans)
