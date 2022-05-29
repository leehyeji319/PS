possible = 'Possible'
impossible = 'Impossible'


def solution(N, M, K, people):
    people.sort()
    for p in range(N):
        if (people[p] // M) * K < p + 1:
            return impossible
    return possible


T = int(input())
for t in range(1, T + 1):
    N, M, K = map(int, input().split())
    people = list(map(int, input().split()))
    print(f"#{t} {solution(N, M, K, people)}")
