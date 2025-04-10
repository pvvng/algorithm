# x는 낮의 횟수
# 달팽이는 낮에 정상에 오를테니 x-1은 미끌어지는 횟수
# 즉 Ax - B(X - 1) = V 가 성립됨
# x로 정리하면 x = (V-B) / (A-B)

A, B, V = map(int, input().split())
x = (V-B)/(A-B)
int_x = int(x)
print(int_x + 1 if int_x != x else int_x)
