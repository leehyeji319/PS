from itertools import combinations

def solution(orders, course):
    answer = []

    for size in course:
        order_dict = {}
        order_combinations = []

        for order in orders:
            order_combinations.extend(list(combinations(sorted(order), size)))

        for order_combination in order_combinations:
            order_str = ''.join(order_combination)
            if order_str in order_dict:
                order_dict[order_str] += 1
            else:
                order_dict[order_str] = 1

        #한개 이상, 가장 많이 뽑힌 갯수 만큼 뽑힌거
        for o in order_dict:
            if order_dict[o] == max([order_dict[o] for o in order_dict]):
                if order_dict[o] > 1:
                    answer.append(o)


    return sorted(answer)


# orders 에 있는 메뉴들 중에서 course개 만큼 뽑아서, 뽑은 것들 중 가장 많은 것 들을 모아서 return
# 조합 을 이용하여 course 배열 안에 있는 원소들의 값 만큼 orders 에서 뽑는다.
# course 배열 안에 있는 원소들을 조합을 이용하여 뽑은 모든 경우의 수를 배열안에 넣고, 각각의 경우가 총 몇번 뽑는지 갯수를 샌다.
# 1개 이상, 가장 많이 뽑힌 갯수 만큼 뽑힌 것들을 모두 return 한다.
