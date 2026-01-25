n = int(input())
lst = [int(input()) for _ in range(n)]
lst.sort()
print("\n".join(map(str, lst)))