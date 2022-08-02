T = 10
for t in range(1, T + 1):
    dump = int(input())
    graph = list(map(int, input().split()))
    while dump > 0:
        graph.sort(reverse=True)    
        graph[0] -= 1
        graph[-1] += 1
        dump -= 1
        if (max(graph) - min(graph)) <= 1:
            break
    answer = max(graph) - min(graph)

    print(f"#{t} {answer}")
