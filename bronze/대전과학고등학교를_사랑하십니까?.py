import sys
input = sys.stdin.readline

m = {
  "animal": "Panthera tigris",
  "tree": "Pinus densiflora",
  "flower": "Forsythia koreana"
}

ans = []

while True:
  text = input().rstrip()
  if text == "end":
    break
  ans.append(m[text])

print("\n".join(ans))
