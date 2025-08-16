ls = [float(input()) for _ in range(int(input()))]
for e in ls:
  print("$" + "{:.2f}".format(e * 80 / 100))