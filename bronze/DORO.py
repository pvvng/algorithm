ans = []
n = int(input())
for txt in input().split():
  txt += "DORO"
  ans.append(txt)
print(" ".join(ans))