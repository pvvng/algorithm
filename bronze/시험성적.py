sc = int(input())
# 90 ~ 100점은 A, 80 ~ 89점은 B, 70 ~ 79점은 C, 60 ~ 69점은 D, 나머지 점수는 F

if(sc>= 90 and sc <= 100):
  print("A")
elif (sc>= 80 and sc <= 89):
  print("B")
elif (sc>= 70 and sc <= 79):
  print("C")
elif (sc >= 60 and sc <= 69):
  print("D")
else :
  print("F")