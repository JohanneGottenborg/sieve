"""Computing primes."""


def sieve(n: int) -> list[int]:
    """
    Compute all the primes up to (and possibly including) `n`.

    `n` must be positive.

    >>> sieve(15)
    [2, 3, 5, 7, 11, 13]

    """
    assert n > 0
    candidates = list(range(2, n + 1))
    primes = []

    # FIXME: fill out this bit

    # for n in candidates:
    #     primes.append(candidates[0])
    #     # print(n)
    #     for m in candidates:
    #         if m // n == 0:
    #             candidates.remove(m)
    #         # print(m)    
    #     print(candidates)
    
    l = list([0]*n)
    for i in l:
        if len(candidates) == 0:
            break
        p = candidates[i]
        primes.append(p)
        candidates.remove(p)
        for c in candidates:
            if c % p == 0:
                candidates.remove(c)
        #print(candidates)

    #print(primes)
    return primes

sieve(15)
