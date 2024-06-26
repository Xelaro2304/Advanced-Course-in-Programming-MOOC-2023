# Write your solution here
def prime_numbers():
    prime = 2
    yield prime
    while True:
        prime +=1
        breaker = False
        for i in range (2, prime):
            if prime % i == 0:
                breaker = True
                break
        if breaker == False:
            yield prime