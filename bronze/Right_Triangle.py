def is_triangle(lst):
  lst.sort()
  return lst[0] ** 2 + lst[1] ** 2 == lst[2] ** 2
ans = []
for i in range(int(input())):
  lst = list(map(int, input().split()))
  ans.append(f"Case #{i+1}: {"YES" if is_triangle(lst) else "NO"}")

print("\n".join(ans))