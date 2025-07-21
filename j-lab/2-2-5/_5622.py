class Telephone():
  def __init__(self):
    self.dial = dict()
    current = ord("A")  
    for i in range(2, 10):
      loop_count = self.__get_loop_count(i)
      for _ in range(loop_count):
        self.dial[chr(current)] = i
        current += 1

  def __get_loop_count(self, current_idx):
    return 4 if current_idx in [7, 9] else 3

  def get_time(self, txt:str):
    total = 0
    for t in txt:
      total += self.dial[t] + 1 # 해당하는 숫자의 +1 만큼이 다이얼에 걸리는 시간
    return total

phone = Telephone()
print(phone.get_time(input()))