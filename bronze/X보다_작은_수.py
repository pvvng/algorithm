n, x = map(int, input().split(" "))
a = list(filter(lambda i : i < x, map(int, input().split(" "))))
print(" ".join(map(str, a)))
