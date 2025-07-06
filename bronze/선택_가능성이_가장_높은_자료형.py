x = int(input())
if (-2**15 <= x <= 2**15 - 1):
  print("short")
elif (-2**31 <= x <= 2**31 - 1):
  print("int")
elif (-2**127 <= x <= 2**127 - 1):
  print("long long")