def solution(name):
    answer = 0

    # 기본 최소 좌우이동 횟수는 길이 - 1
    min_move = len(name) - 1

    for i, char in enumerate(name):
        # 해당 알파벳 변경 최솟값 추가
        answer += min(ord(char) - ord('A'), ord('Z') - ord(char) + 1)

        # 해당 알파벳 다음부터 연속된 A문자열 찾기
        next_idx = i + 1
        while next_idx < len(name) and name[next_idx] == 'A':
            next_idx += 1

        # 기존, 연속된 A의 왼쪽시작 방식, 연속된 A의 오른쪽시작 방식 비교 및 갱신
        min_move = min([min_move, 2 * i + len(name) - next_idx, i + 2 * (len(name) - next_idx)])
    # 알파벳 변경(상하이동) 횟수에 좌우 이동 횟수 추가
    answer += min_move
    return answer


print(solution("JEROEN"))
