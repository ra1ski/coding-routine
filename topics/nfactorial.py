def nfactrial(n: int) -> int:
    if n < 2:
        return 1

    return n * nfactrial(n-1)

print(nfactrial(5))


