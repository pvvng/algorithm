# Equilateral :  세 변의 길이가 모두 같은 경우
# Isosceles : 두 변의 길이만 같은 경우
# Scalene : 세 변의 길이가 모두 다른 경우
# 가장 긴 변의 길이보다 나머지 두 변의 길이의 합이 길지 않으면 삼각형의 조건을 만족하지 못한다.
def triangle(a, b, c):
  ls = [a, b, c]  
  ls.sort()
  if ls[0] + ls[1] <= ls[2]:
    return "Invalid"
  if a == b == c:
    return "Equilateral"
  if a == b or b == c or a == c:
    return "Isosceles"
  return "Scalene"

ans = []
while True:
  a, b, c = map(int, input().split())
  if a == b == c == 0:
    break
  ans.append(triangle(a, b, c))
  
print("\n".join(ans))
