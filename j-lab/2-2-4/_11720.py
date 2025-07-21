def sol(N:int, nums:str) -> int:
  cnt = 0
  for i in range(N):
    cnt += int(nums[i])
  return cnt

N = int(input())
nums = input()
print(sol(N, nums))