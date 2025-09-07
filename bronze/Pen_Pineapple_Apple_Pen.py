def sol(n:int, stuffs: list[str]):
  target = "pPAp"
  cnt = 0
  idx = 0

  while idx < n - 3:
    test = stuffs[idx] + stuffs[idx + 1] + stuffs[idx + 2] + stuffs[idx + 3]
    if test == target:
      idx += 3
      cnt += 1
    idx += 1
    
  return cnt

n = int(input())
stuffs = list(input())
print(sol(n, stuffs))
# count 메서드로도 해결 가능
# print("".join(stuffs).count("pPAp"))