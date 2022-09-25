def solution(today, terms, privacies):
    answer = []
    terms_dict = {}
    YEARTODAY = 28 * 12
    MONTHTODAY = 28
    for term in terms:
        name, t = term.split(" ")
        terms_dict[name] = int(t) * MONTHTODAY

    new_privacies = []
    for privacy in privacies:
        date, name = privacy.split(" ")
        year, month, day = map(int, date.split("."))
        _today = year * YEARTODAY + month * MONTHTODAY + day

        if name in terms_dict:
            _today += terms_dict[name]

        new_privacies.append(_today)

    year, month, day = map(int, today.split("."))
    new_today = year * YEARTODAY + month * MONTHTODAY + day

    for i in range(len(new_privacies)):
        if int(new_today) - int(new_privacies[i]) >= 0:
            answer.append(i + 1)

    return answer


print(solution("2020.01.01", ["Z 3", "D 5"],
               ["2019.01.01 D", "2019.11.15 Z", "2019.08.02 D", "2019.07.01 D", "2018.12.28 Z"]))
# print(solution("2022.05.19", ["A 6", "B 12", "C 3"], ["2021.05.02 A", "2021.07.01 B", "2022.02.19 C", "2022.02.20 C"]))
