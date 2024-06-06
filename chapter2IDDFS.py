#깊이제한탐색
def IDDFS(root, goal, max_depth):
    for depth in range(max_depth + 1):
        found, _ = DFS(root, goal, depth)
        if found is not None:
            return found
    return None

def DFS(node, goal, depth):
    if depth == 0 and node != goal:
        return None, True
    if node == goal:
        return node, False
    if depth > 0:
        children = generate_children(node)
        for child in children:
            found, remaining = DFS(child, goal, depth - 1)
            if found is not None:
                return found, False
            if not remaining:
                return None, False
    return None, True

def generate_children(node):
    children = []
    if node == 'A':
        children = ['B', 'C', 'D']
    elif node == 'B':
        children = ['E', 'F']
    elif node == 'C':
        children = ['G', 'H']
    elif node == 'D':
        children = ['I']
    elif node == 'E':
        children = ['U']

    return children

result = IDDFS('A', 'U', 4)
if result is not None:
    print("Found:", result)
else:
    print("Not Found")
