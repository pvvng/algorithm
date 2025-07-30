current = 1
while True:
  loop_count = int(input())
  if loop_count == 0:
    break
  village = set()
  for _ in range(loop_count):
    village.add(input())
  print(f"Week {current} {len(village)}")
  current += 1
