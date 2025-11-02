n = int(input())
T = list(map(int, input().split()))
time = sum(T) + (len(T) - 1) * 8
print(time // 24, time % 24)
