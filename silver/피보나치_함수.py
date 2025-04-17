n = int(input())
ls = [int(input()) for _ in range(n)]
fib_dict = { 0 : [1, 0], 1 : [0, 1] }

next_key = 2
for v in ls:
  for i in range (next_key, v + 1):
    fib_dict[i] = [
      fib_dict[i - 1][0] + fib_dict[i - 2][0], 
      fib_dict[i - 1][1] + fib_dict[i - 2][1]
    ]
    next_key = i

  print(fib_dict[v][0], fib_dict[v][1])