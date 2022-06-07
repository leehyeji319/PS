import collections 

def solution(id_list, report, k):
    answer = []
    dict_report = collections.defaultdict(set)
    dict_target = collections.defaultdict(int)
    report_list = []
    mail_list = []
    
    dict_answer = {}
    for idl in id_list:
        dict_answer[idl] = 0
    
    for r in report:
        reporter, target = r.split()
        dict_report[reporter].add(target)

    for target in dict_report.values():
        for t in target:
            dict_target[t] += 1
    
    for ans, cnt in dict_target.items():
        if cnt >= k:
            report_list.append(ans)
    
    for i, j in dict_report.items():
        for k in report_list:
            if k in j:
                mail_list.append(i)
    
    for ml in mail_list:
        dict_answer[ml] += 1

            
    for a in dict_answer.values():
        answer.append(a)
    
    return answer

print(solution(["muzi", "frodo", "apeach", "neo"], ["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"], 2))