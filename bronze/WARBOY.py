# 경쟁사 제품의 가격 A, 경쟁사 제품의 성능 B, WARBOY의 가격 C
# 가성 * 가격 = 성능
# 가격 대비 성능이 경쟁사 제품의 3배
# WARBOY의 성능

a, b, c = map(int, input().split())
print(3 * c * (b // a))
