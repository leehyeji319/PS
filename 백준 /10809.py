import string

# 알파벳을 담을 list
# find함수 사용
str = input()
alpha = list(string.ascii_lowercase)

for a in alpha:
    print(str.find(a), end = ' ')