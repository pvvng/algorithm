# X사 : 1리터당 A엔.
# Y사 : 기본요금은 B엔이고, 사용량이 C리터 이하라면 요금은 기본요금만 청구된다. 
#       사용량이 C리터가 넘었을 경우 기본요금 B엔에 더해서 추가요금이 붙는다. 
#       추가요금은 사용량이 C리터를 넘었을 경우 1리터를 넘었을 때마다 D엔이다.

# 첫 번째 줄에는 X사의 1리터당 요금 A가 입력된다.
# 두 번째 줄에는 Y사의 기본요금 B가 입력된다.
# 세 번째 줄에는 Y사의 요금이 기본요금이 되는 사용량의 상한 C가 입력된다.
# 네 번째 줄에는 Y사의 1리터 당 추가요금 D가 입력된다.
# 다섯 번째 줄에는 JOI군의 집에서 사용하는 한 달간 수도의 양 P가 입력된다.

def sol(x: int, y: tuple[int, int, int], p):
  x_fee = p * x

  y_limit, y_basic, y_extra = y
  y_fee = y_basic + (max(0, p - y_limit) * y_extra)

  return min(x_fee, y_fee)

x_basic = int(input())
y_basic = int(input())
y_limit = int(input())
y_extra = int(input())
p = int(input())
print(sol(x_basic, (y_limit, y_basic, y_extra), p))
