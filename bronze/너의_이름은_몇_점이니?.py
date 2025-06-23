x = int(input())
st = input()
cnt = 0
for i in range(x):
  cnt += ord(st[i]) - 64
print(cnt)