# case 1
def init_dict():
  alphabets = dict()
  for i in range(ord("a"), ord("z") + 1):
    alphabets[i] = 0
  return alphabets

def sol(txt: str):
  alphabets = init_dict()

  for char in txt:
    alphabets[ord(char)] += 1

  for key in alphabets:
    print(alphabets[key], end=" ")

sol(input())

# case2: 숏코딩
bets = [0] * 26
for char in input():
  bets[ord(char) - 97] += 1

print(*bets)