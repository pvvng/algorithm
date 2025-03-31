# 01 또는 OI가 포함되어 있다면 문장 끝에 한 개의 영일이 이모티콘을 넣기로 했다. 
# 이때, 홍보 글에 영일이 이모티콘을 총 몇 번 넣어야 하는지 구하여라.

try_count = int(input())
count = 0

for i in range(try_count):
  text = input()
  if "01" in text or "OI" in text:
    count += 1

print(count)