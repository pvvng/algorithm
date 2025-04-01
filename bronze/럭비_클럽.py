# 나이가 17세보다 많거나, 몸무게가 80kg -> 성인부
# 성인부 회원이면 'Senior', 청소년부 회원이면 'Junior'


while(True):
  name, age, weight = input().split()
  weight, age = map(int, (weight, age))
  if(name == "#" or weight + age == 0): break
  state = ""
  if(age > 17 or weight >= 80):
    state += "Senior"
  else : state += "Junior"
  print(name + " " + state)