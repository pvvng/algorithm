k_idx = y_idx = 0
for i in range(int(input())):
  txt = input()
  if txt == "korea":
    k_idx = i
  if txt == "yonsei":
    y_idx = i

print("Yonsei " + ("Won!" if y_idx < k_idx else "Lost..."))