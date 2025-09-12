def sol(n:int, k:int):
  b = 0
  while n > 0:
    # k 진수 변환
    d = n % k  
    n //= k

    # d를 b의 가장 낮은 자릿수에 추가
    # 기존 b를 k(자릿수)배 해주고 마지막 자리에 추가할 요소 집어넣기
    b = b * k + d 

  return b   

n, k = map(int, input().split())
print(sol(n, k))
