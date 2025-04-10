ls = []
for _ in range(3):
  ls.append(input())

zz = ["Fizz", "Buzz", "FizzBuzz"]
x = -1
for i in range(len(ls)):
  if ls[i] not in zz:
    x = (3-i) + int(ls[i])
    break

if x % 3 == 0 and x % 5 == 0:
  print(zz[2])
elif x % 3 == 0 and x % 5 != 0:
  print(zz[0])
elif x % 3 != 0 and x % 5 == 0:
  print(zz[1])
else:
  print(x) 
