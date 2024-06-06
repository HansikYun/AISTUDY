#언덕 등반 기법
def hill_climbing(root):
    current = root
    while True:
        # 현재 노드의 자식 노드들을 생성
        neighbors = generate_neighbors(current)
        # 평가 함수 값이 가장 높은 자식 노드 선택
        neighbor = max(neighbors, key=lambda x: value(x))
        # 만일 모든 위치가 현 위치보다 낮다면 그 곳을 정상이라고 판단
        if value(neighbor) <= value(current):
            return current
        # 현 위치가 정상이 아니라면 확인된 위치 중 가장 높은 곳으로 이동
        current = neighbor

# 평가 함수
def value(node):
    # 노드의 평가 함수 값 반환
    pass

# 현재 노드의 자식 노드 생성 함수
def generate_neighbors(node):
    # 노드의 자식 노드들을 생성하여 반환
    pass
