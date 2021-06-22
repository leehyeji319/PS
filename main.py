summary = 0
for i in range(1,10):
  summary += i
print(summary)

for _ in range(5):
  print("Hello World")


a = [1, 4, 3]
print("기본 리스트 : ", a)

#리스트에 원소 삽입
a.append(2)
print("삽입 : ", a)

#오름차순 정렬
a.sort()
print("오름차순 정렬: ", a)

#내림차순 정렬
a.sort(reverse = True)
print("내림차순 정렬: ", a)

a = [4, 3, 2, 1]

#리스트 원소 뒤집기 
a.reverse()
print("원소 뒤집기: ", a)

#특정 인덱스에 데이터 추가 
a.insert(2,3)
print("인덱스 2에 3 추가 : ", a)

#특정 값인 데이터 개수 세기
print("값이 3인 데이터 개수 : ", a.count(3))

#특정 값 데이터 삭제
a.remove(1)
print("값이 1인 데이터 삭제: ", a)

#리스트에서 특정값을가지는 원소를 모두 제거하기
a = [1, 2, 3, 4, 5, 5, 5]
remove_set = {3,5} #집합 자료형 (집합 자료형은 추후에 다시 다룹니다)

#remove_list 에 포함되지 않은 값만을 저장
#i가 remove_set에 포함되어있지 않다면,,
result = [i for i in a if i not in remove_set]
print(result)


#문자열 자료형
a = 'Hello World'
print(a)

#문자열은 특정 인덱스의 값을 변경할 수 없다.(immutable)

a = "Hello"
b = "World"
print(a + " " + b)

a = "String"
print(a * 3)




#튜플 사용 예제
a = (1, 2, 3, 4, 5, 6, 7, 8, 9)

#네 번째 원소만 출력
print(a[3])

#두 번째 원소부터 네 번째 원소까지
print(a[1:4])

