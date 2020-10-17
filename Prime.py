# 입력받는 수가 소수인지 판별하는 문제

n = int(input(""))
# 정수입력
def isPrime(n):
    if n == 2:
        return True # 예외처리
    if n % 2 == 0:
        return False #짝수는 모두 소수가아니다, 하지만 2는 예외처리되어있음
    for i in range(2, n):
        if n % i == 0 :
            return False #n 보다 작은수로 나눠지면 소수가 아님
    return True
#통과하면 소수로 판별난다.

print(isPrime(n))


