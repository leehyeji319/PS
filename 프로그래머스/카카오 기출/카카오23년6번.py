from collections import deque


def bfs(n, m, x, y, r, c, k):
    global answer
    q = deque()
    q.append((x, y, [], 0))

    while q:
        to_x, to_y, move, cnt = q.popleft()

        if cnt == k:
            if to_x == r and to_y == c:
                string = ''.join(move)
                if string < answer:
                    answer = string
                    return
            continue

        for d in range(4):
            nr = to_x + dr[d]
            nnc = to_y + dc[d]

            if 1 <= nr <= n and 1 <= nnc <= m:
                if d == 0:
                    char = "d"
                elif d == 1:
                    char = "l"
                elif d == 2:
                    char = "r"
                elif d == 3:
                    char = "u"
                q.append((nr, nnc, move + [char], cnt + 1))


answer = "z"
dr = [1, 0, 0, -1]
dc = [0, -1, 1, 0]


def solution(n, m, x, y, r, c, k):
    bfs(n, m, x, y, r, c, k)
    return answer if answer != "z" else "impossible"


# print(solution(3,4,2,3,3,1,5))


print(solution(2, 2, 1, 1, 2, 2, 2))
