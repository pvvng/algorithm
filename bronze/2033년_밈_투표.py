ls = [
  "Never gonna give you up",
  "Never gonna let you down",
  "Never gonna run around and desert you",
  "Never gonna make you cry",
  "Never gonna say goodbye",
  "Never gonna tell a lie and hurt you",
  "Never gonna stop",
]

ps = True

for _ in range(int(input())):
  t = input()
  if t not in ls:
    ps = False
    break

print("No" if ps else "Yes")
