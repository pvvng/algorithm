def sol(n, r, c, se):
  if n == 1:
    return se + r * 2 + c # (r->2, c->1)
  
  half = 2 ** (n-1) # 현재 n에 대한 절반
  split_count = 4 ** (n-1) # 분할된 사분면의 요소 총 개수
  mul = (r >= half) * 2 + (c >= half) # se에 대한 증가값 (r->2, c->1)
  se += mul * split_count
  if r >= half: 
    r -= half # r 위치 축소
  if c >= half:
    c -= half # c 위치 축소

  return sol(n-1, r, c, se)

n, r, c = map(int, input().split())
print(sol(n, r, c, 0))