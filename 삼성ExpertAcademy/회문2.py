T = 10


def rotation_90(graph):
    graph_90 = [[0] * 100 for _ in range(100)]
    for row in range(100):
        for column in range(100):
            graph_90[column][99 - row] = graph[row][column]
    return graph_90


def check_palindrome(s):
    MAX = 0
    for i in range(len(s)):
        for j in range(i + 1, len(s) + 1):
            if s[i:j] == s[i:j][::-1]:
                if MAX < len(s[i:j]):
                    MAX = len(s[i:j])
    return MAX


for t in range(1, T + 1):
    N = int(input())
    graph = [input() for _ in range(100)]
    graph_90 = rotation_90(graph)
    MAX = 0
    for s in graph:
        if MAX < check_palindrome(s):
            MAX = check_palindrome(s)
    for s in graph_90:
        if MAX < check_palindrome(s):
            MAX = check_palindrome(s)
    print(f"#{t} {MAX}")


