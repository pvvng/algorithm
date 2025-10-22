x = int(input())
y = input()

ans = []
for i in range(len(y)-1, -1, -1):
  ans.append(str(x * (int(y[i]))))
ans.append(str(x * int(y)))

print("\n".join(ans))