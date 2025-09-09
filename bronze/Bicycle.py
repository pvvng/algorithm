def sol(T, a, b, x, y):
  free = {"a": 30, "b": 45}
  def f(type, p, q):
    return 21 * p * max(0, T - free[type]) + q
  return (f("a", x, a), f("b", y, b))

a = int(input())
x = int(input())
b = int(input())
y = int(input())
T = int(input())

print(*sol(T, a, b, x, y))
