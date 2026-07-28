entry = input("Ingrese números separados por comas: ")

def is_prime(o):
    if o <= 1:
        return False
    
    for i in range(2, o):
        if o % i == 0:
            return False
    
    return True


def filter_primes(num_list):
    primes = []
    
    for number in num_list:
        if is_prime(number):
            primes.append(number)
    
    return primes


num_list = [int(x) for x in entry.split(",")]

result = filter_primes(num_list)

print("Los números primos son:", result)