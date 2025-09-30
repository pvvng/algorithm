def sol(T: list[int]):
  p = [0] * 101
  p[1], p[2], p[3] = 1, 1, 1
  p[4], p[5] = 2, 2
  for i in range(6, 101):
    p[i] = p[i-1] + p[i-5] 
  ans = []
  for t in T:
    ans.append(str(p[t]))
  return "\n".join(ans)

T = [int(input()) for _ in range(int(input()))]
print(sol(T))