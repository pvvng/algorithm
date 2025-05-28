# 술하고 같이 초밥을 먹거나 점심 식사가 아닐 때는 초밥의 밥알을 280개
# 점심 식사이면서 술과 같이 먹지 않을때는 초밥의 밥알을 320개
# 12 ~ 16 점심

time, drink = map(int, input().split())
if(bool(drink)): print(280)
elif (12 <= time <= 16): print(320)
else: print(280)