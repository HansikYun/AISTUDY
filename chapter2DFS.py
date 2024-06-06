#깊이우선탐색
def DFS(root, goal):
    open_list = [root]
    closed_list = []

    while open_list:
        x = open_list.pop(0)

        if x == goal:
            return "SUCCESS"
        else:
            children = generate_children(x)

            closed_list.append(x)

            for child in children:
                if child not in open_list and child not in closed_list:
                    open_list.insert(0, child)

    return "FAIL"

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

result = DFS('A', 'U')
print(result)
