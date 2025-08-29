def sol(crt: list,  cnt: int):
  if len(crt) == cnt:
    return 1
  
  ans = 0
  # 기본 탐색 범위
  s, e = 1, 9

  # 직전 요소에 따라 탐색 범위 조절 
  if len(crt) > 0:
    s = max(crt[-1] - 2, s)
    e = min(crt[-1] + 2, e)
  
  for i in range(s, e + 1):
    crt.append(i)
    ans += sol(crt, cnt)
    crt.pop()

  return ans

n = int(input())
print(sol([], n))
