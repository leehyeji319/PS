T = int(input())


def dfs(graph, v, visited, ans):
    global answer
    visited[v] = True
    ans += 1
    #최대값 갱신
    if answer < ans:
        answer = ans

    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited, ans)
    visited[v] = False


for t in range(1, T + 1):
    n, m = map(int, input().split())
    board = [[] for _ in range(n + 1)]
    visited = [False] * (n + 1)
    answer = 0
    for _ in range(m):
        a, b = map(int, input().split())
        board[a].append(b)
        board[b].append(a)
    #시작 노드를 다르게 해서 최대 길이 찾기
    for i in range(n):
        dfs(board, i, visited, 0)
    print(f"#{t} {answer}")
