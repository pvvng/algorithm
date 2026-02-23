import sys
input = sys.stdin.readline

n = int(input())

stack = []
for _ in range(n):
  cmd, value, cmd_at = input().split()
  cmd_at = int(cmd_at)
  if cmd == "type":
    stack.append((cmd, value, cmd_at))
    continue
  stack.append((cmd, int(value), cmd_at))

# undo x y
# y-x ~ y 까지의 행동 삭제
ans = ""
while stack:
  c, v, t = stack.pop()
  if c == "undo":
    while stack and stack[-1][2] >= t-v:
      stack.pop()
  if c == "type":
    ans = v + ans 

print(ans)