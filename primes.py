"""List of prime numbers generator."""
"""ENTER YOUR SOLUTION HERE!"""

def primes(number_of_primes):
    list = []
    newlist = []
    while 1:
        for i in range(2, 100):
            for j in range(2, i):
                if j == i:
                    pass
                else:
                    if i%j == 0:
                        list.append(i)
            if i not in list:
                newlist.append(i)
            
            if len(newlist) == int(number_of_primes):
                break
            else:
                continue
        break
    return newlist
