ls = [input() for _ in range(int(input()))]
print(len(list(filter(lambda x : x.startswith("C") ,ls))))