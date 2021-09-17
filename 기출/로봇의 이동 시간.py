# 롯정
def solution(direction, pos):
    answer = 0
    # pos = start position
    direction = [0] + list(direction)
    while True:
        if pos == 0 or pos >= len(direction):
            break
        if direction[pos] == '<':
            direction[pos] = '>'
            pos -= 1
            answer += 1
        elif direction[pos] == '>':
            direction[pos] = '<'
            pos += 1     
            answer += 1
    return answer


solution('>><', 1)