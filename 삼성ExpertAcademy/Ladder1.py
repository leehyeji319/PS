T = 10; 
for t in range (1, T + 1):
    n = int(input())
    ladder = [list(map(int, input().split())) for _ in range(100)]
    answer = 0
    col = 0
    row = 99
    
 
    for j in range(100):
        if ladder[99][j] == 2:
            col = j #57
            break
            
    # dx = [1, -1, 0]
    # dy = [0, 0, -1]
    
    while True:
        if row == 0:
            answer = col
            break
            
         # 현재 칸을 0으로 해서 지나온 지점을 check
        ladder[row][col] = 0
        if row < 0 or col < 0 or col > 100 or row:
            continue
        # 왼쪽 으로 가는 경우
        if ladder[row][col - 1] == 1:
            col -= 1
        # 오른쪽 으로 가는 경우
        elif ladder[row][col + 1] == 1:
            col += 1
        # 위로 가는 경우
        elif ladder[row - 1][col] == 1:
            row -= 1
            
        

    print(f"#{t} {answer}")