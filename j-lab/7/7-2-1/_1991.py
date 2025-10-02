import sys
input = sys.stdin.readline

def sol(edges):
  tree = {}
  for p, lc, rc in edges:
    tree.setdefault(p, (lc, rc))

  ans = []
  ans.append(preorder("A", tree))
  ans.append(inorder("A", tree))
  ans.append(postorder("A", tree))

  return "\n".join(ans)

def preorder(node, tree): # 전위
  if node == '.': return ""
  return node + preorder(tree[node][0], tree) + preorder(tree[node][1], tree)

def inorder(node, tree): # 중위
  if node == '.': return ""
  return inorder(tree[node][0], tree) + node + inorder(tree[node][1], tree)

def postorder(node, tree): # 후위
  if node == '.': return ""
  return postorder(tree[node][0], tree) + postorder(tree[node][1], tree) + node

n = int(input())
edges = [input().split() for _ in range(n)]
print(sol(edges))