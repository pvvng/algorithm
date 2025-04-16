n = int(input())
ls = sorted(list(map(int, input().split())))

prev_sum = 0
cnt = 0

for i in ls:
  prev_sum += i
  cnt += prev_sum

print(cnt)