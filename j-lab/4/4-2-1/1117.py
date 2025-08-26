import sys
sys.setrecursionlimit(10**6)

A = input()

# 재귀
def sol1(current: str, idx: int):
  if idx == 0:
    return A[idx]
  return A[idx] + sol1(current, idx - 1)

print(int(sol1("", len(A) - 1)))

# 반복문
def sol2(A):
  ans = ""
  for i in range(len(A) - 1, -1 , -1):
    if ans == "" and A[i] == "0":
      continue
    ans += A[i]

  return int(ans)

print(sol2(A))
