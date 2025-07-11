# 1 ~ end 구간까지의 리스트를 구하고 해당 리스트에서 1~start, 1~end 범위를 추출하면 O(n)으로도 정답을 구할 수 있을듯
# 1 ~ end 구간 리스트를 O(n)으로 생성해야함

start, end = map(int, input().split())
start -= 1

ls = []
current = 1
cnt = 0
for i in range(end):
  # 반복 횟수 1 증가
  cnt += 1
  # 현재 값 추가
  ls.append(current)
  # 현재 값과 반복 횟수가 동일해지는 순간은 초기화 순간임
  if current == cnt: 
    # 다음 인덱스에서 정상적인 값을 반영할 수 있도록 초기화
    current += 1
    cnt = 0

print(sum(ls[start:end]))