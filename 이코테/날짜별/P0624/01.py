# 사전 자료형
data = dict()
data['사과'] = 'Apple'
data['바나나'] = 'Banana'
data['코코넛'] = 'Coconut'

# 키 데이터만 담은 리스트
key_list = data.keys()
# 값 데이터만 담은 리스트
values_list = data.values()
print(key_list)
print(values_list)

# 각 키에 따른 값을 하나씩 출력
for key in key_list:
  print(data[key])



a = dict()
a['홍길동'] = 97
a['이순신'] = 98

print(a)

b = {
  '홍길동' : 97,
  '이순신' : 98
}


print(b)

key_list = list(b.keys())
print(key_list)

#집합 자료형 초기화 방법 1
data = set([1, 1, 2, 3, 4, 4, 5])
print(data)

#집합 자료형 초기화 방법 2
data = {1, 1, 2, 3, 4, 4, 5}
print(data) 


a