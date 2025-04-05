a, b = map(int, input().split())
d, c = map(int, input().split())
arr = [a, b, c ,d]
circ = []

for i in range(4):
  circ.append(arr[0]/arr[3] + arr[1]/arr[2])
  e = arr.pop()
  arr.insert(0, e)

maxy = max(circ)
print(circ.index(maxy))