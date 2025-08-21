# 고기가 얼어 있고 온도가 0℃ 미만일 때 : 온도가 C초에 1℃씩 오른다.
# 고기가 얼어 있고 온도가 정확히 0℃일 때 : 얼어 있지 않은 상태로 만드는(해동하는) 데 D초가 걸린다.
# 고기가 얼어 있지 않을 때 : 온도가 E초에 1℃씩 오른다.

def sol(a, b, c, d, e):
  cnt = 0
  if a <= 0:
    cnt += (-a) * c + d
    a = 0
  cnt += (b - a) * e

  return cnt

ls = [int(input()) for _ in range(5)]
print(sol(*ls))