from collections import deque

def solution(cards1, cards2, goal):
    for g in goal:
        if len(cards1) > 0 and g == cards1[0]:
            cards1 = cards1[1:]
        elif len(cards2) > 0 and g == cards2[0]:
            cards2 = cards2[1:]
        else:
            return 'No'
    return 'Yes'