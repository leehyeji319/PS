import sys

input = sys.stdin.readline


def bfs():
    for teacher in teachers:
        for d in range(4):
            nr, nc = teacher[0], teacher[1]
            while 0 <= nr < N and 0 <= nc < N:
                if board[nr][nc] == "O":
                    break

                if board[nr][nc] == "S":
                    return False

                nr += dr[d]
                nc += dc[d]

    return True


def set_obstacle(obstacle_cnt):
    # bfs 감시 피하기 성공 여부
    global flag
    # 장애물이 세개 설치가 됐다면
    if obstacle_cnt == 3:
        # bfs를 돌려서 모든 선생님 감시 피하기 성공 여부를 반환받는다.
        if bfs():
            flag = True
            return
    else:
        # 장애물이 세개가 아니라면 장애물을 설치한다.
        for i in range(N):
            for j in range(N):
                if board[i][j] == 'X':
                    board[i][j] = 'O'
                    set_obstacle(obstacle_cnt + 1)
                    board[i][j] = 'X'


N = int(input())
board = [list(input().split()) for _ in range(N)]

teachers = []
for r in range(N):
    for c in range(N):
        if board[r][c] == 'T':
            teachers.append([r, c])

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

flag = False

set_obstacle(0)

if flag:
    print("YES")
else:
    print("NO")