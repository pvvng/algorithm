# loop
def sol(txt:str):
  ans = ""
  for i in range(len(txt)):
    if i % 2 != 0:
      ans += txt[i]
  return ans

# slicing
def sol2(txt:str):
  return txt[1::2] # 1번째 문자열부터 2개씩 증가

txt = input()
print(sol2(txt))