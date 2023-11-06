def dfs(start, graph, visited, check):
        cnt = 1
        visited[start] = True
        for adj in graph[start]:
            if not visited[adj] and check[start][adj]:
                cnt += dfs(adj, graph, visited, check)
        return cnt

    


def solution(n, wires):
    answer = int(1e9)

    
    graph = [[] for _ in range(n + 1)]
    check = [[True] * (n + 1) for _ in range(n + 1)]
    
    for s, e in wires:
        graph[s].append(e)
        graph[e].append(s)

    # 차례대로 순회하면서 송전탑 전선을 짤라보기
    for s, e in wires:
        visited = [False] * (n + 1)
        check[s][e] = False

        # 전선을 짜르고 나서 각 각 몇개인지 찾아보기
        cnt_s = dfs(s, graph, visited, check)
        cnt_e = dfs(e, graph, visited, check)
        check[s][e] = True 

        answer = min(abs(cnt_s - cnt_e), answer)
    
    return answer


# print(solution(9, [[1,3],[2,3],[3,4],[4,5],[4,6],[4,7],[7,8],[7,9]]))
# print(solution(4, [[1,2],[2,3],[3,4]]))
# print(solution(7, [[1,2],[2,7],[3,7],[3,4],[4,5],[6,7]]))