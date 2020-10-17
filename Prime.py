n = int(input(""))

def isPrime(n):
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(2, n):
        if n % i == 0 :
            return False
    return True

print(isPrime(n))


