def solution(n, times):
    answer = 0
    time_min, time_max = 1, max(times) * n

    while time_min <= time_max:
        time_mid = (time_min + time_max) // 2
        people = 0

        for time in times:
            people += time_mid // time

            if people >= n:
                break

        if people >= n:
            answer = time_mid
            time_max = time_mid - 1
        else:
            time_min = time_mid + 1

    return answer
