def win_condition(board, w):
        for row in board:
            if row == [w, w, w]:
                return True
        
        for col in range(3):
            if [board[row][col] for row in range(3)] == [w, w, w]:
                return True
        
        if [board[0][0], board[1][1], board[2][2]] == [w, w, w]:
            return True
        
        if [board[2][0], board[1][1], board[0][2]] == [w, w, w]:
            return True
        
        return False

def solution(board):
    board = [list(row) for row in board]

    o_cnt = 0 
    x_cnt = 0
    
    for r in range(3):
        for c in range(3):
            if board[r][c] == 'O':
                o_cnt += 1
            elif board[r][c] == 'X':
                x_cnt += 1

                
    if not (o_cnt == x_cnt or o_cnt == x_cnt + 1): 
        return 0

    if win_condition(board, 'O') and win_condition(board, 'X'):
        return 0
    
    if win_condition(board, 'O') and o_cnt != x_cnt + 1:
        return 0
    
    if win_condition(board, 'X') and o_cnt != x_cnt:
        return 0
    
    return 1

    
    


print(solution(["O.X", ".O.", "..X"]))