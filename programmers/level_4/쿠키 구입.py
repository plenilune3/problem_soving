def solution(cookie):
    answer = -1
    length = len(cookie)

    for i in range(length - 1):
        first_value, first_index = cookie[i], i
        second_value, second_index = cookie[i + 1], i + 1

        while True:
            if first_value == second_value and first_value > answer:
                answer = first_value

            if first_index > 0 and first_value <= second_value:
                first_index -= 1
                first_value += cookie[first_index]
            elif second_index < length - 1 and second_value <= first_value:
                second_index += 1
                second_value += cookie[second_index]
            else:
                break

    return answer if answer != -1 else 0
