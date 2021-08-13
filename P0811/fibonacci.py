# 피보나치 수열: 단순 재귀 코드

#피보나치 함수(Fibonacci Function)을 재귀함수로 구현
def fibo(x):
    if x == 1 or x == 2:
        return 1
    return fibo(x - 1) + fibo(x - 2)
print(fibo(4))

# 피보나치 함수 다이나믹 프로그래밍 1. 최적 부분구조 : 큰 문제를 작은 문제로 , 2. 중복되는 부분 문제 : 동일한 작은 문제 반복적
# 메모이 제이션 : 다이나믹 프로그래밍을 구현하는 방법 중 하나 
# 한 번 계산한 결과를 메모리 공간에 메모하는 기법입니다. 같은 문제를 다시 호출하면 메모했던 결과를 그대로 가져옵니다. 값을 기록해놓는것을 cashing 캐싱이라고 합니다.
# 다이나믹 프로그래밍의 전형적인 방법은 보텀업 방식이빈다. 결과 저장용 리스트는 DP테이블이라고 부릅니다.