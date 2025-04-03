ls = []
n = int(input())
for _ in range(n):
  quiz = input()
  cont = 0
  sum = 0
  for i in range (len(quiz)):
    c = quiz[i]
    if(c == "O"):
      cont += int(c == "O")
    else:
      cont = 0
    sum += cont
  ls.append(sum)

for i in ls:
  print(i)