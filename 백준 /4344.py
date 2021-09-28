t = int(input())

for _ in range(t):
    student = list(map(int,(input().split())))
    stu_num = student[0]
    student = student[1:len(student)]
    avg = float(sum(student)) / float(stu_num)
    cnt = 0

    for i in student:
        if i > avg:
            cnt += 1
        global radio
        radio = format((float(cnt) / float(stu_num) * 100), ".3f")
    print(str(radio) + '%')