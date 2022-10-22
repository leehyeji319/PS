import sys
input = sys.stdin.readline

def dfs(tree, v, visited, cnt): #트리, 현재 노드, 방문배열, 비행기개수

    #현재노드를 방문한다
    visited[v] = True

    for i in tree[v]:
        if not visited[i]:
            cnt = dfs(tree, i, visited, cnt + 1)

    return cnt



T = int(input())

for tc in range(1, T + 1):
    N, M = map(int, input().split()) # 국가의 수, 비행기 종류
    tree = [[] for _ in range(N + 1)]

    for _ in range(M):
        a, b = map(int, input().split())
        tree[a].append(b)
        tree[b].append(a)
    visited = [False] * (N + 1)

    print(dfs(tree, 1, visited, 0))
