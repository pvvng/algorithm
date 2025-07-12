# 세 각의 크기가 모두 60이면, Equilateral
# 세 각의 합이 180이고, 두 각이 같은 경우에는 Isosceles
# 세 각의 합이 180이고, 같은 각이 없는 경우에는 Scalene
# 세 각의 합이 180이 아닌 경우에는 Error

def sol(angs : list[int]):
  cnt = sum(angs)
  angs_set = set(angs)

  if cnt != 180:
    return "Error"

  tp = {
    1: "Equilateral",
    2: "Isosceles",
    3: "Scalene"
  }

  return tp[len(angs_set)]

angs_list = [int(input()) for _ in range(3)]
print(sol(angs_list))