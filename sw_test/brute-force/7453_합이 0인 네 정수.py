def two_pointer(AB, CD, N, S):
    left_length = N * N
    left_index = 0
    right_index = N * N - 1
    answer = 0

    while left_index < left_length and right_index >= 0:
        left_value = AB[left_index]
        right_value = CD[right_index]

        if left_value + right_value == S:
            left_count = 0
            right_count = 0

            while left_index < left_length and left_value == AB[left_index]:
                left_count += 1
                left_index += 1
            while right_index >= 0 and right_value == CD[right_index] :
                right_count += 1
                right_index -= 1

            answer += left_count * right_count

        elif left_value + right_value > S:
            right_index -= 1
        else:
            left_index += 1

    return answer


def solution():
    N = int(input())
    array = [[] for i in range(4)]
    AB, CD = [], []

    for i in range(N):
        temp = list(map(int, input().split()))
        for j in range(4):
            array[j].append(temp[j])
    for i in range(N):
        for j in range(N):
            AB.append(array[0][i] + array[1][j])
            CD.append(array[2][i] + array[3][j])

    AB.sort()
    CD.sort()

    # PyPy3으로 통과...
    # Python3으로 통과하려면 Counter(Dictionary)를 활용해야 한다.
    answer = two_pointer(AB, CD, N, 0)
    print(answer)


solution()

