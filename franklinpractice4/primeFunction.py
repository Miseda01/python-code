def isPrime(n, divisor = 2):
    if n <= 0:
        return False
    elif n <= 3 :
        return True
    elif n % divisor == 0:
        return False
    elif divisor * divisor > n:
        return True
    else :
        return isPrime(n, divisor + 1)


def oddEven(num):
    if num % 2 == 0:
        print(f"{num} Even")
    else:
        print(f"{num} odd")


def primeNumber(start,end):
    for num in range(start,end+1):
        if isPrime(num):
            print("Prime number", num)
        else:
            oddEven(num)


#Calling The Function iSPrime
num = 20
end = 60
primeNumber(num, end)
