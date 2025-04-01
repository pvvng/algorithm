# 모음의 개수를 세는 프로그램을 작성하시오. 모음은 'a', 'e', 'i', 'o', 'u'이며 대문자 또는 소문자

moum = "aeiou"
moum = moum + moum.upper()
moum = list(moum)

while(True):
  text = input()
  if text == "#":
    break
  cnt = 0
  for i in moum:
    cnt += text.count(i)
  print(cnt)