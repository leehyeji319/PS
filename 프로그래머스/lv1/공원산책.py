import sys

def solution(park, routes):
    answer = []
    board = []
    
    s_r = 0
    s_c = 0

    height = len(park)
    width = len(park[0])

    for i in range(len(park)):
        l = []
        for j in range(len(park[i])):
            if park[i][j] == 'S':
                s_r = i
                s_c = j
            l.append(park[i][j])
        board.append(l)

    # for b in board:
    #     print(b)
    # print(s_r)
    # print(s_c)

    d = {"N": [-1, 0], "S": [1, 0], "W": [0, -1], "E": [0, 1]}



    now_r = s_r
    now_c = s_c

    for route in routes:
        Flag = True
        direction, distance = route.split(" ")

        for i in range(1, int(distance) + 1):
            dr = d[direction][0] * i
            dc = d[direction][1] * i

            nr = dr + now_r
            nc = dc + now_c

            if nr < 0 or nr >= height or nc < 0 or nc >= width or board[nr][nc] == 'X':
                Flag = False
                break
        if not Flag:
            continue
        now_r += d[direction][0] * int(distance)
        now_c += d[direction][1] * int(distance)

    
    answer.append(now_r)
    answer.append(now_c)
    

    
    return answer

print(solution(["SOO","OOO","OOO"], ["E 2","S 2","W 1"]))
print(solution(["SOO","OXX","OOO"], ["E 2","S 2","W 1"]))
print(solution(["OSO","OOO","OXO","OOO"], ["E 2","S 3","W 1"]))