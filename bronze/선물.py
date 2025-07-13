n, x = map(int, input().split())
ss = list(map(int, (input().split())))

st = []
for i in range(n - 1):
  st.append((ss[i] + ss[i+1]) * x)

print(min(st))