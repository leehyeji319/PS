def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

#집합 합치기 부모기준
def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b


T = int(input())

for tc in range(1, T + 1):
    #노드 개수, 간선개수 입력
    v, e = map(int, input().split())
    parent = [0] * (v + 1) #부모 테이블 초기화

    #모든 간선을 담을 리스트와, 최종 비용을 담을 변수
    edges = []
    result = 0

    #부모 테이블상에서 부모를 자기 자신으로 초기화
    for i in range(1, v + 1):
        parent[i] = i

    #모든 간선에 대한 정보 입력받기
    for _ in range(e):
        a, b, cost = map(int, input().split())
        #비용순 정렬위해 튜플 첫번째 원소 비용으로 설정
        edges.append((cost, a, b))
    edges.sort()

    #간선하나씩 확인
    for edge in edges:
        cost, a, b = edge
        #사이클이 발생하지 않는 경우에만 집합에 포함
        if find_parent(parent, a) != find_parent(parent, b):
            union_parent(parent, a, b)
            result += cost
    print(f"#{tc} {result}")