def check(x, k, stones, length):
    count = k

    for i in range(length):
        if x > stones[i]:
            count -= 1  # down count.
        else:
            count = k  # revert count.

        if count == 0:
            return False

    return True


def solution(stones, k):
    answer = 0
    length = len(stones)
    people_min, people_max = 0, 200000000

    while people_min <= people_max:
        middle = (people_min + people_max) // 2

        if check(middle, k, stones, length):
            answer = middle
            people_min = middle + 1
        else:
            people_max = middle - 1

    # answer = people_max if check(people_max, k, stones, length) else people_min
    return answer

