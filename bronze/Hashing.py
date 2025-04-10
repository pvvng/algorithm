import sys
input = sys.stdin.readline

r = 31
M = 1234567891

n = int(input())
s = input()

sm = 0
for i in range(n):
  sm += (ord(s[i]) % 96) * (r ** i)

print(sm % M)