T = 1; 
for t in range (1, T + 1):
    n = int(input())
    ladder = [list(map(int, input().split())) for _ in range(100)]
    answer = 0
    dx = [1, -1, 0]
    dy = [0, 0, -1]
    for i in range(100):
        for j in range(100):
            if ladder[i][j] == 2:
                start_y = i #99
                start_x = j #57
                break
            
    while True:
        for i in range(3):
            nx = dx[i] + start_x
            ny = dy[i] + start_y
            
            if ny == 0:
                answer = nx
                print(nx)
                break
            
            if ladder[ny][nx] == 1:
                ladder[start_x][start_y] = 0
                start_x = nx
                start_y = ny
                continue
        if answer != 0: break

    print(f"#{t} {answer}")