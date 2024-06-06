#A*알고리즘
def astar(root, goal):
    open_list = [root]
    closed_list = []
    while open_list:
        # open 리스트에서 가장 평가 함수의 값이 좋은 노드 선택
        x = min(open_list, key=lambda node: f(node, goal))
        if x == goal:
            return "SUCCESS"
        else:
            # x의 자식 노드 생성
            children = generate_children(x)
            # x를 closed 리스트에 추가
            closed_list.append(x)
            for child in children:
                # 자식 노드가 open이나 closed 리스트에 없으면
                if child not in open_list and child not in closed_list:
                    # 자식 노드의 평가 함수값 f(n) = g(n) + h(n)을 계산
                    f_value = g(child) + h(child, goal)
                    # 자식 노드들을 open 리스트에 추가
                    open_list.append(child)
    return "FAIL"

# g 함수
def g(node):
    # 노드의 현재까지의 비용 반환
    pass

# h 함수 (휴리스틱 함수)
def h(node, goal):
    # 노드로부터 목표까지의 예상 비용 반환
    pass

# f 함수 (평가 함수)
def f(node, goal):
    # f(n) = g(n) + h(n)
    return g(node) + h(node, goal)

# 노드의 자식 노드 생성 함수
def generate_children(node):
    # 노드의 자식 노드들을 생성하여 반환
    pass
