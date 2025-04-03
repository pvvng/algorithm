n = int(input())
a = []

for i in range (n):
  h, w, guest = map(int, input().split(" "))
  room_nums = []
  rows = 0  # 행 (세로)
  cols = 0  # 열 (가로)
  for num in range(guest):
    room_nums.append((rows + 1) * 100 + cols + 1)
    rows += 1
    if(rows > h - 1):
      rows = 0
      cols += 1
  a.append(room_nums[len(room_nums) - 1])

for v in a:
  print(v)
