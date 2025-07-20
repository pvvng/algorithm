class Cups:
  def __init__(self, ball_index = 1, cups_length = 3):
    self.cups = [0] * cups_length
    self.cups[ball_index - 1] = 1

  def swap(self, t1, t2):
    t1 -= 1; t2 -= 1
    if self.__canSwap(t1) or self.__canSwap(t2):
      temp = self.cups[t1]
      self.cups[t1] = self.cups[t2]
      self.cups[t2] = temp

  def __canSwap(self, t) -> bool:
    return self.cups[t] == 1

  def find(self):
    return self.cups.index(1) + 1

cups = Cups()

for _ in range(int(input())):
  x, y = map(int,input().split())
  cups.swap(x, y)

print(cups.find())
