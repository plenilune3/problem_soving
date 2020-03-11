N = int(input())


def get_primes(N):
    is_prime = [True for i in range(N+1)]
    is_prime[0] = is_prime[1] = False
    k = int(N**0.5) + 1

    for i in range(2, k):
        if is_prime[i]:
            for j in range(i+i, N+1, i):
                is_prime[j] = False

    return [i for i in range(2, N+1) if is_prime[i]]


def solve(N):
    primes = get_primes(N)
    length = len(primes)
    answer = 0
    subtotal = 0
    start = 0
    end = 0

    while True:
        if subtotal >= N:
            subtotal -= primes[start]
            start += 1
        elif end == length:
            break
        else:
            subtotal += primes[end]
            end += 1

        if subtotal == N:
            answer += 1

    print(answer)


solve(N)
