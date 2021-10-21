import re

n = input()
formula = re.split("[+-]", n)
formula = list(map(int, formula))

op = []
result = 0

for i in n:
    if i == '-':
        op.append(i)
    elif i == '+':
        op.append(i)

if '-' in op:
    index = op.index('-')

    for i in range(0, index + 1):
        result += formula[i]

    for j in range(index + 1, len(formula)):
        result -= formula[j]
        
    print(result)

else:
    print(sum(formula))




