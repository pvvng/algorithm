x = list(input())
key = ord("C") ^ ord(x[0])
print("".join(list(map(lambda x : chr(ord(x) ^ key), x))))