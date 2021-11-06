# 음식을 판 순수익 계산
from collections import Counter

def solution(ings, menu, sell):
    answer = 0
    ings_ = {}
    menu_ = {}
    sell_ = {}
    for ing in ings:
        a, b = ing.split()
        b = int(b)
        ings_[a] = b
    print(ings_)
    for m in menu:
        a, b, c = m.split()
        c = int(c)
        b = Counter(b)
        used = 0
        for i, v in b.items():
            used += ings_[i] * v
        benefit = c - used
        menu_[a] = benefit
    print(menu_)
    for s in sell:
        a, b = s.split()
        b = int(b)
        sell_benefit = menu_[a] * b
        sell_[a] = sell_benefit
    print(sell_)
    
    for i in sell_.values():
        answer += i
    return answer

solution(["r 10", "a 23", "t 124", "k 9"],["PIZZA arraak 145", "HAMBURGER tkar 180", "BREAD kkk 30", "ICECREAM rar 50", "SHAVEDICE rar 45", "JUICE rra 55", "WATER a 20"], ["BREAD 5", "ICECREAM 100", "PIZZA 7", "JUICE 10", "WATER 1"])