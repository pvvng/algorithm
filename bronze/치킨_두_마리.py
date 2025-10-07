x, y = map(int, input().split())
t = int(input())
b = x + y
print(b - 2 * t if 2 * t <= b else b)