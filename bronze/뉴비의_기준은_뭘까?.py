# 뉴비를 1학년 혹은 2학년인 학생
# 올드비는 N학년 이하이면서 뉴비가 아닌 학생
# TLE은 뉴비도 아니고 올드비도 아닌 학생

# NEWBIE!
# OLDBIE!
# TLE!

# m이 target
n, m = map(int, input().split())
if m == 1 or m == 2:
  print("NEWBIE!")
elif m <= n:
  print("OLDBIE!")
else:
  print("TLE!")