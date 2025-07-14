n = int(input())

cnt = 0
st = set()
for i in range(5, 0, -1):
  left = i
  right = n - i
  if (left < 0 or right < 0):
    continue
  if (left > 5 or right > 5):
    continue
  if left in st or right in st:
    continue
  st.add(left)
  st.add(right)
  cnt += 1

print(cnt)