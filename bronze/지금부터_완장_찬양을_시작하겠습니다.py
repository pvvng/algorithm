n, k = map(int, input().split())
atd = input()

streak = 0
max_streak = 0

for s in atd:
  if s == "0":
    streak += 1
    max_streak = max(max_streak, streak)
  else:
    streak = 0

print(int(max_streak < k))