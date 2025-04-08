# 자연수n의 분해합m
# m은 n의 생성자
n = int(input())
cons = 0
for i in range(n):
  ls = [int(ch) for ch in str(i)]
  if(i + sum(ls) == n):
    cons = i
    break

print(cons)