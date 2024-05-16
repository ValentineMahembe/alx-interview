#!/usr/bin/python3
"""
Prime game implementation
"""


def isWinner(x, nums):
    """
    Implementation
    """
    if x < 1 or not nums:
        return None

    # Maximum possible value of n
    max_n = max(nums)

    # Sieve of Eratosthenes to find all primes up to max_n
    primes = [True] * (max_n + 1)
    primes[0] = primes[1] = False
    p = 2
    while (p * p <= max_n):
        if primes[p] is True:
            for i in range(p * p, max_n + 1, p):
                primes[i] = False
        p += 1

    # List of prime numbers up to max_n
    prime_nums = [i for i, is_prime in enumerate(primes) if is_prime]

    maria_wins = 0
    ben_wins = 0

    # Function to determine the winner of a single round
    def play_game(n):
        # Mark primes and their multiples
        remaining = list(range(1, n + 1))
        turn = 0  # 0 for Maria, 1 for Ben

        for prime in prime_nums:
            if prime > n:
                break
            if prime in remaining:
                turn ^= 1
                remaining = [x for x in remaining if x % prime != 0]

        return "Maria" if turn == 1 else "Ben"

    # Play each game
    for n in nums:
        winner = play_game(n)
        if winner == "Maria":
            maria_wins += 1
        else:
            ben_wins += 1

    # Determine the overall winner
    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
