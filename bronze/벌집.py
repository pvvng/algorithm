n = int(input())

end, idx = 1, 1

while n > end:
  end += 6 * idx
  idx += 1

print(idx)