# 행(Row)이 3개인 2차원 리스트로 인접 리스트 표현
board = [[] for _ in range(3)]

#노드 0에 연결된 노드 정보 저장(노드, 거리)
board[0].append((1, 7))
board[0].append((2, 5))

# 노드 1에 연결된 노드 정보 저장
board[1].append((0, 7))

# 노드 2에 연결된 노드 정보 저장
board[2].append((0, 5))

print(board)