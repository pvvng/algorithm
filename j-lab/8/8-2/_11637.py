import sys
input = sys.stdin.readline

def sol(nums):
  total = sum(nums)
  v = []
  for i in range(len(nums)):
    v.append((i+1, nums[i]))
  v.sort(key=lambda x : (-x[1], x[0]))
  if v[0][1] == v[1][1]:
    return "no winner"
  status = "minority" if v[0][1] <= total // 2 else "majority"
  return f"{status} winner {v[0][0]}"

t = int(input())
ans = []
for _ in range(t):
  n = int(input())
  nums = [int(input()) for _ in range(n)]
  ans.append(sol(nums))
print("\n".join(ans))
