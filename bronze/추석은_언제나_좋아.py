def sol():
  x = int(input())
  if x >= 1000000:
    return (int(x * 0.2), int(x * 0.8))
  if x >= 500000:
    return (int(x * 0.15), int(x * 0.85))
  if x >= 100000:
    return (int(x * 0.1), int(x * 0.9))
  return (int(x * 0.05), int(x * 0.95))

print(*sol())