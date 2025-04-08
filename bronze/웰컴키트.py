# 티셔츠는 S, M, L, XL, XXL, 그리고 XXXL의 6가지 사이즈가 있습니다. 
# 티셔츠는 같은 사이즈의 T장 묶음으로만 주문할 수 있습니다.
# 펜은 한 종류로, 
# P자루씩 묶음으로 주문하거나 한 자루씩 주문할 수 있습니다.
import math

n = int(input())
ts = list(map(int, input().split()))
t, p = map(int, input().split())

cnt = 0
for i in ts :
  cnt += math.ceil(i / t)
  
print(cnt)
print(f"{n // p} {n % p}")