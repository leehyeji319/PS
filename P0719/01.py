#자주 사용하는 내장 함수 
#sum()
result = sum([1, 2, 3, 4, 5])
print(result)

#min(), max()
min_result = min(7, 3, 5, 2)
max_result = max(7, 3, 5, 2)
print(min_result, max_result)

#eval()
#사람이 입장해서 수식으로 표현된 수식이 있을때 실제 수식으로 반환해주는 함수
result = eval("(3+5)*7") 
print(result)

#sorted()
result = sorted([9, 1, 8, 5, 4])
reverse_result = sorted([9, 1, 8, 5, 4], reverse=True)
print(result)
print(reverse_result)

#sorted() with key
array = [('홍길동', 35), ('이순신', 75), ('아무개', 50)]
result = sorted(array, key=lambda x: x[1], reverse=True)
print(result)

