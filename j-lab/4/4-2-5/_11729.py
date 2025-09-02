import sys
sys.setrecursionlimit(10**6)

# 실패 
# 사유: 어려움
def hanoi(n, frm, to, aux, out):
    if n == 1:
        out.append(f"{frm} {to}")
        return
    hanoi(n-1, frm, aux, to, out)
    out.append(f"{frm} {to}")
    hanoi(n-1, aux, to, frm, out)

n = int(sys.stdin.readline())
moves = []
hanoi(n, 1, 3, 2, moves)
print(len(moves))
print("\n".join(moves))