n = int(input())
ans =[]
for _ in range(n):
  # k층에 n호
  k = int(input())
  n = int(input())
  floor = [[i for i in range (1, n + 1)]]
  for i in range(k):
    n_a = []
    for j in range(n):
      n_a.append(sum(floor[-1][:j+1]))
    floor.append(n_a)
  ans.append(floor[-1][-1])

for v in ans:
  print(v)