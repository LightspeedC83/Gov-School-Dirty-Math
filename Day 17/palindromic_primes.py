
def SieveOfEratosthenes(num): #seive of eratothsenes --> https://www.geeksforgeeks.org/python-program-for-sieve-of-eratosthenes/#
    prime = [True for i in range(num+1)]
    # boolean array
    p = 2
    while (p * p <= num):

        # If prime[p] is not
        # changed, then it is a prime
        if (prime[p] == True):

            # Updating all multiples of p
            for i in range(p * p, num+1, p):
                prime[i] = False
        p += 1

    # output the prime numbers
    output = []
    for p in range(2, num+1):
        if prime[p]:
            str_prime = str(p)
            if str_prime==str_prime[::-1]:
                # output.append(p)
                print(p)
    # return(output)

# start of the program
depth = 100000
primes = SieveOfEratosthenes(depth)
