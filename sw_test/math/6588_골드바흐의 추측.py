from sys import stdin, stdout
from math import sqrt

number_max = 1000000

is_prime = [False, False] + [True] * (number_max - 1)
temp = int(sqrt(number_max)) + 1

for i in range(2, temp):
    if is_prime[i]:
        for j in range(i+i, number_max+1, i):
            is_prime[j] = False

while True:
    n = int(stdin.readline())

    if n == 0:
        break
    else:
        for i in range(3, number_max+1):
            if is_prime[i]:
                j = n - i
                if is_prime[j]:
                    stdout.write(str(n) + ' = ' + str(i) + ' + ' + str(j) + '\n')
                    break

