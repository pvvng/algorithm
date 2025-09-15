# n을 k 진수로 변환한 수를 a
# a의 각 자리의 수의 합을 k 진수로 변환하여 출력
def sol(n: int, k: int):
  t = 0
  while n > 0:
    t += n % k
    n //= k
  ans = ""
  while t > 0:
    ans = str(t % k) + ans
    t //= k
  return ans

n, k = map(int, input().split())
print(sol(n, k))