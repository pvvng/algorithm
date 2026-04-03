# 각 자릿수에 대해서 해당 숫자가 짝수인지 홀수인지를 확인한다. 숫자 0은 짝수이다.
# 모든 자릿수에 대해서 홀짝 판별이 완료되면 전체 짝수의 개수와 홀수의 개수를 비교한다.
# 짝수의 개수가 홀수의 개수보다 더 많으면 주어진 수는 짝짝수이다. 홀수의 개수가 짝수의 개수보다 더 많으면 홀홀수이다.

n = int(input())
k = input()

hh = jj = 0
for i in range(n):
  if int(k[i]) % 2 == 0:
    jj += 1
  else:
    hh += 1

if hh > jj:
  print(1)
elif hh < jj:
  print(0)
else:
  print(-1)