import sys
input = sys.stdin.readline

s = set(["0","6"])
ans = 0
t = int(input())
for _ in range(t):
  score = list(input())
  for i in range(len(score)):
    if score[i] in s:
      score[i] = "9"
  ans += min(100, int("".join(score)))

print(int(ans/t + 0.5))

