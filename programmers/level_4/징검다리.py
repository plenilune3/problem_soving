def solution(distance, rocks, n):
    answer = 0
    rocks.sort()
    left, right = 1, distance

    while left <= right:
        count = 0
        prev = 0
        middle = (left + right) // 2

        for rock in rocks:
            if rock - prev < middle:
                count += 1
            else:
                prev = rock
        else:
            if distance - prev < middle:
                count += 1

        if count <= n:
            answer = max(middle, answer)
            left = middle + 1
        else:
            right = middle - 1

    return answer

