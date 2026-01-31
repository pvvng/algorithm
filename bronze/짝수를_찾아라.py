import sys
input = sys.stdin.readline

def sol(lst):
  filtered = list(filter(lambda x: x%2==0, lst))
  return f"{sum(filtered)} {min(filtered)}"

ans = []
for _ in range(int(input())):
  ans.append(sol(list(map(int, input().split()))))

print("\n".join(ans))
