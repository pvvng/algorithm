mobis = list("MOBIS")
check = set(list(input()))
ok = True
for m in mobis:
  if m not in check:
    ok = False
    break
print("YES" if ok else "NO")