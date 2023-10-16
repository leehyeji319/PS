# 모든 달은 28일까지 있다고 가정합니다.
from datetime import datetime
import math

def solution(today, terms, privacies):
    answer = []
    ONE_MONTH = 28
    ONE_YEAR = 12
    d = dict()
    n_year, n_month, n_day = map(int, today.split("."))
    today_date = datetime(n_year, n_month, n_day)

    for term in terms:
        category, month = term.split(" ")
        d[category] = int(month)
    
    for i in range(len(privacies)):
        collected_date, category = privacies[i].split(" ")
        t_year, t_month, t_day = map(int, collected_date.split("."))

        days_to_add = d[category] * ONE_MONTH - 1
        t_day += days_to_add
        t_month += math.floor(t_day / ONE_MONTH)
        t_day %= ONE_MONTH
        if t_day == 0:
            t_day = ONE_MONTH
            t_month -= 1
        t_year += math.floor(t_month / ONE_YEAR)
        t_month %= ONE_YEAR
        if t_month == 0:
            t_month = ONE_YEAR
            t_year -= 1
        target_date = datetime(t_year, t_month, t_day)

        if today_date > target_date:
            answer.append(i + 1)

    return answer



print(solution("2022.05.19", ["A 6", "B 12", "C 3"], 
               ["2021.05.02 A", "2021.07.01 B", "2022.02.19 C", "2022.02.20 C"]	))