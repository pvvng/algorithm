def lower_last_char(string: str) -> str:
  if string[-1].isupper():
    return string[:len(string) - 1] + string[-1].lower()
  return string

def is_continous(prev:str, char:str, target:set) -> bool:
  return prev in target and char in target

def sol(S: str):
  target = set(["A", "a"])
  prev = ""
  new_s = ""
  for char in S:
    if is_continous(prev, char, target): 
      new_s = lower_last_char(new_s)
    else:
      new_s += char
    prev = char

  return new_s

def sol2(S: str) -> str:
  target = set(["A", "a"])
  T = ""
  i = 0

  while i < len(S):
    # a, A가 아니면 그냥 집어넣기
    if S[i] not in target:
      T += S[i]
      i += 1
      continue
    
    # 연속적인 문자열 찾기
    j = i + 1
    while j < len(S):
      # 다음 문자열이 a, A 아니면 정지
      if S[j] not in target:
        break
      j += 1
    

    # 연속적인 문자열의 길이가 없을때
    if j - i == 1:
      T += S[i] # 일반적으로 추가
    # 연속적인 문자열일때
    else:
      T += S[i].lower()
    
    i = j

  return T

S = input()
# print(sol(S))
print(sol2(S))
