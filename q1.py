def checkIsPrime(n):
    isPrime = True
    i = 2
    while i <= (n**0.5):
        if n % i == 0:
            isPrime = False
        i+=1

    return isPrime


def getPrimeNumbers(n):
    primes = {x for x in range(n+1) if checkIsPrime(x)}
    return primes
