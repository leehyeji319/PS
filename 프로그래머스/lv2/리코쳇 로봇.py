from collections import deque
def solution(board):
    answer = 0
    R = len(board)
    C = len(board[0])

    sr, sc = 0, 0
    for r in range(R):
        for c in range(C):
            if board[r][c] == 'R':
                sr, sc = r, c

    dr = [-1, 1, 0, 0] #상하좌우
    dc = [0, 0, -1, 1]
    
    visited = [[0] * C for _ in range(R)]

    def bfs(): 
        q = deque()
        q.append([sr, sc])
        visited[sr][sc] = 1

        while q:
            r, c = q.popleft()

            if board[r][c] == 'G':
                return visited[r][c] - 1
            
            for d in range(4):
                nr, nc = r, c
                while True:
                    nr += dr[d]
                    nc += dc[d]
                    if (0 > nr or R <= nr or 0 > nc or C <= nc) \
                        or (0 <= nr < R and 0 <= nc < C and board[nr][nc] == 'D'):
                        nr -= dr[d]
                        nc -= dc[d]
                        break
                if not visited[nr][nc]:
                    visited[nr][nc] = visited[r][c] + 1
                    q.append([nr,nc])
        return -1 
    
    return bfs()

print(solution(["...D..R", ".D.G...", "....D.D", "D....D.", "..D...."]))