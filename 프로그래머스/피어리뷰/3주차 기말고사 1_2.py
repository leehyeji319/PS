from collections import deque

def solution(rows, columns, max_virus, queries):
    graph = [[0] * columns for i in range(rows)]
    
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    
    def infection(row, col, infected):
        if row < 0 or row >= rows or col < 0 or col >= columns:
            return
        
        if (row, col) in infected:
            return
        
        infected.append((row, col))
        
        if graph[row][col] < max_virus:
            graph[row][col] += 1
        else:
            for i in range(4):
                nx = row + dx[i]
                ny = col + dy[i]
                infection(nx, ny, infected)
        return
    
    for query in queries:
        infected = []
        row, col = query
        row -= 1
        col -= 1
        infection(row, col, infected)     
        
     
    return graph

print(solution(3, 4, 2, [[3,2],[3,2],[2,2],[3,2],[1,4],[3,2],[2,3],[3,1]]))