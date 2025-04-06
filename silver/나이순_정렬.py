import sys
input = sys.stdin.readline

n = int(input())
ls = []

for i in range(n):
  age, name = input().split()
  ls.append((i, int(age), name))

# 나이 순, 나이가 같으면 가입한 순
ls.sort(key=lambda x : (x[1], x[0]))

for v in ls:
  print(f"{v[1]} {v[2]}")