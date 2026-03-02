import sys
input = sys.stdin.readline
print(["N","E","S","W"][sum([int(input()) for _ in range(10)]) % 4])
