# 차:13, 포:7, 마:5, 상:3, 사:3, 졸:2
# 척이는 선수인 초나라로, 은규는 후수인 한나라 (+1.5)
# 초나라 cocjr0208, 한나라 ekwoo
score = [13, 7, 5, 3, 3, 2]
c = list(map(int, input().split()))
h = list(map(int, input().split()))
ct = 0; ht = 1.5
for i in range(6):
  ct += c[i] * score[i]
  ht += h[i] * score[i]
print("ekwoo" if ct < ht else "cocjr0208")

