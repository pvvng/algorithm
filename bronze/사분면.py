note = {
  "Q1": 0,
  "Q2": 0,
  "Q3": 0,
  "Q4": 0,
  "AXIS": 0
}

for _ in range(int(input())):
  x, y = map(int, input().split())
  if x == 0 or y == 0:
    note["AXIS"] += 1
  if x > 0 and y > 0:
    note["Q1"] += 1
  if x < 0 and y > 0:
    note["Q2"] += 1
  if x < 0 and y < 0:
    note["Q3"] += 1
  if x > 0 and y < 0:
    note["Q4"] += 1

for key in note:
  print(f"{key}: {note[key]}")