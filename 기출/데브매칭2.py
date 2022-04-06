def solution(grid):
    answer = -1
    l = len(grid[0])
    arr = []
    for i in range(len(grid)):
        arr_s = []
        for j in range(l):
            arr_s.append(grid[i][j])
        arr.append(arr_s)
        
    print(arr)
        
    a_c = arr.count('a')
    b_c = arr.count('b')
    c_c = arr.count('c')
    
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    
    
       
    
    
    print(a_c, b_c, c_c)

    return answer

print(solution(["??b", "abc", "cc?"]))