def fizzBuzz():
    for num in range(1,101):
        if num % 3== 0 and num % 5 == 0:
            print(f'FIZZBUZZ {num}')
        elif num % 3 == 0:
            print(f'FIZZ {num}')
        elif num % 5 == 0:
            if num % 2 == 0:
                print(f'BUZZ {num}')
        else:
            print(num)

# calling the function fissBuzz
fizzBuzz()   

def isPrime(n, divisor=2):
    if n <= 0:
        return False
    elif n<=3:
        return True
    elif n % divisor==0:
        return False
    elif divisor * divisor > n:
        return True
    else :
        return isPrime(n,divisor +1)

num = 17 
x = isPrime(num)
print(x)   

