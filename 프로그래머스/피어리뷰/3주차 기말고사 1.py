#세균번식

from collections import deque

def solution(rows, columns, max_virus, queries):
    
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    
    graph = [[0] * columns for i in range(rows)]

    queries = deque(queries)

    while queries:
        x, y = queries.popleft()
        x -= 1 
        y -= 1
        log = [] # 한 턴인지 확인하는 로그
        recursive(rows, columns, max_virus, queries, dx, dy, graph, x, y, log)    
    
    return graph


def recursive(rows, columns, max_virus, queries, dx, dy, graph, x, y, log):
    if (x, y) in log:
        return
    
    if 0 <= x < rows and 0 <= y < columns:
        log.append((x, y))
        
        if graph[x][y] < max_virus:
            graph[x][y] += 1
        else:
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                recursive(rows, columns, max_virus, queries, dx, dy, graph, nx, ny, log)
    else:
        return

print(solution(3, 4, 2, [[3,2],[3,2],[2,2],[3,2],[1,4],[3,2],[2,3],[3,1]]))