#!/usr/bin/python3
"""Determine the winner of the Prime Game."""


def isWinner(x, nums):
    """Return the player who wins the most rounds."""
    if x <= 0 or not nums:
        return None

    rounds = min(x, len(nums))
    max_n = max(nums[:rounds])

    is_prime = [True] * (max_n + 1)

    if max_n >= 0:
        is_prime[0] = False

    if max_n >= 1:
        is_prime[1] = False

    number = 2

    while number * number <= max_n:
        if is_prime[number]:
            multiple = number * number

            while multiple <= max_n:
                is_prime[multiple] = False
                multiple += number

        number += 1

    prime_counts = [0] * (max_n + 1)
    count = 0

    for number in range(max_n + 1):
        if is_prime[number]:
            count += 1

        prime_counts[number] = count

    maria_wins = 0
    ben_wins = 0

    for n in nums[:rounds]:
        if prime_counts[n] % 2 == 1:
            maria_wins += 1
        else:
            ben_wins += 1

    if maria_wins > ben_wins:
        return "Maria"

    if ben_wins > maria_wins:
        return "Ben"

    return None
