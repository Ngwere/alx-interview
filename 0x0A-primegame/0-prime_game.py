#!/usr/bin/python3
"""The prime game"""

def isWinner(x, nums):
    """
    A prime game with two players Maria and Ben are playing.

    Args:
        x (int): number of rounds
        nums (list): an array of size n
    """
    if x <= 0 or nums is None:
        return None
    if x != len(nums):
        return None

    maria_wins = 0 
    ben_wins = 0

    for i in nums:
        playing(i, maria_wins, ben_wins)
    if maria_wins < ben_wins:
        return "Ben"
    return "Maria"

def playing(n, maria_wins, ben_wins):
    nums = []
    for i in range(n+1):
        nums.append(i)
    prime = getPrimes(n)
    while prime:
        maria_play = play(n,prime,nums)
        if (len(prime) == 1):
            ben_wins +=1
        if (not maria_play):
            ben_wins +=1
        ben_play = play(n,prime,nums)
        if (not ben_play):
            maria_wins +=1

def play(n, prime, nums):
    """"if there is a pime choose and optimize prime"""
    if (prime and n>1):
        max_prime = max(prime)
        for i in range(max_prime, n+1, max_prime):
            nums.remove(i)
        prime.remove(max_prime)
        return True
    return False
   
def getPrimes(n):
    """Create and array of primes less than n
    
    Args: 
        n (int): the last integer
    """
    prime = [True for i in range(n+1)]
    p = 2
    while (p * p <= n):
 
        # If prime[p] is not
        # changed, then it is a prime
        if (prime[p] == True):
 
            # Update all multiples of p
            for i in range(p * p, n+1, p):
                prime[i] = False
        p += 1
    prime_list = []
    for p in range(2, n+1):
        if prime[p]:
            prime_list.append(p)
    return prime_list
