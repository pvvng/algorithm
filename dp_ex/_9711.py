import sys
input = sys.stdin.readline

def dp(p, q):
  a, b = 1, 1
  for _ in range(p-2):
    a, b = b % q, (a + b) % q
  return b % q

n = int(input())

ans = []
for i in range(1, n+1):
  p, q = map(int, input().split())
  ans.append(f"Case #{i}: {dp(p, q)}")

print("\n".join(ans))
