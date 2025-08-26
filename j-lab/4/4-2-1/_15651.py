import sys
input = sys.stdin.readline

def sol(iterator: list, target: int, current: list[str] = []):
  if len(current) == target:
    print(" ".join(current))
    return

  for i in iterator:
    current.append(i)
    sol(iterator, target, current)
    current.pop()

n, m = map(int, input().split())
iterator = [str(i+1) for i in range(n)]
sol(iterator, m)