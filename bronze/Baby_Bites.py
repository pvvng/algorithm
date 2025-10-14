n = int(input())
a = input().split()
st = True
for i in range(n):
  if a[i] == "mumble":
    continue
  if int(a[i]) != i + 1:
    st = False
    break

print("makes sense" if st else "something is fishy")
