
def is_prime(prime):
    for n in range(2, prime):
        if prime % n == 0:
            return False
    return True


print(is_prime(15))


def get_prime_numbers(n):
    prime_numbers_dict = {}

    for x in range(2,n+1):
        prime_numbers_dict[x] = True

    for i in range(2, int(n**0.5)+1):
        print(int(n**0.5)+1)
        if prime_numbers_dict[i]:
            for multiple in range(i*i, n+1, i):
                prime_numbers_dict[multiple] = False

    primes = [i for i in prime_numbers_dict if prime_numbers_dict[i]]

    print(primes)

get_prime_numbers(100)




