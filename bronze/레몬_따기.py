N = int(input())
lemons = list(map(int, input().split()))
for i in range(N):
  lemons[i] -= (N - i)
print(max(lemons))