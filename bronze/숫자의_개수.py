nums = {}
for i in range(10):
  nums[str(i)] = 0

multify = 1
for i in range(3):
  multify *= int(input())

for v in list(str(multify)):
  nums[v] += 1

for key in (nums):
  print(nums[key])