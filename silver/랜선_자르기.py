import sys
input = sys.stdin.readline

k, n = map(int, input().split())
ls = []
for _ in range(k):
  ls.append(int(input()))

miny = 1
maxy = max(ls)
res = -1

while miny <= maxy:
  mid = (miny + maxy) // 2
  cnt = sum(v // mid for v in ls)
  if cnt >= n:
    res = mid # 최댓값 후보
    miny = mid + 1 # 더 큰 값도 되는지 보기
  else:
    # 지금의 mid는 너무 큰 값이라서 랜선을 N개 만들 수 없음
    # 그럼 mid 이상은 전부 불가능한 값
    # 따라서 탐색 범위를 maxy = mid - 1로 줄여야 함
    maxy = mid - 1

print(res)
