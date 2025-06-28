price = 3
total = 0
for _ in range(3):
  total += price * int(input())
  price += 1
print(total)