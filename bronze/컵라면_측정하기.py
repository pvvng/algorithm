k = int(input())
d1, d2 = map(int, input().split())
print(k**2 - (abs(d1 - d2) / 2) ** 2)