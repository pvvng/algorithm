ls = ["MatKor", "WiCys", "CyKor", "AlKor", "$clear"]
x = input()
print(list(filter(lambda s: s.startswith(x), ls))[0])