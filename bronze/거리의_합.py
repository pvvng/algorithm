n = int(input())
X = list(map(int, input().split()))
X.sort()
total = [0]
# 0번째 total 값 구하기
for i in range(1, n):
  total[0] += X[i] - X[0]
# 0번째 total 값을 기준으로 누적합
# 점화식 -> 
#   i번째 total = (i-1)번째 total - (i번째 value - (i-1)번째 value) * (n-i) // (0 < i < n-1)
for i in range(1, n - 1):
  total.append(total[i - 1] - (X[i] - X[i - 1]) * (n - i))
print(sum(total) * 2)
