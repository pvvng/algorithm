n, m = map(int, input().split())
ans = []
for _ in range(n):
  line = input()
  length = len(line)
  new_line = ["."] * length
  for i in range(length // 2):
    if line[i] != ".":
      new_line[i] = line[i]
      new_line[length-i-1] = line[i]
    if line[length-i-1] != ".":
      new_line[length-i-1] = line[length-i-1]
      new_line[i] = line[length-i-1]

  ans.append("".join(new_line))
print("\n".join(ans))
  