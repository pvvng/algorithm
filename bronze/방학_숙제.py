L = int(input())
A = int(input())
B = int(input())
C = int(input())
D = int(input())

X = max(A // C + int((A % C) > 0), B // D +int((B % D) > 0))
print(L-X)