def subsequence_sum(sum, index, end_index, sequence, result):
    if index == end_index:
        result.append(sum)
    else:
        subsequence_sum(sum, index+1, end_index, sequence, result)
        subsequence_sum(sum+sequence[index], index+1, end_index, sequence, result)


def two_pointer(left_subsequence, right_subsequence, S):
    right_index = len(right_subsequence) - 1
    left_length = len(left_subsequence)
    left_index = 0
    answer = 0

    while left_index < left_length and right_index >= 0:
        left_subsequence_sum = left_subsequence[left_index]
        right_subsequence_sum = right_subsequence[right_index]

        if left_subsequence_sum + right_subsequence_sum == S:
            left_count = 0
            right_count = 0

            while left_index < left_length and left_subsequence[left_index] == left_subsequence_sum:
                left_count += 1
                left_index += 1
            while right_index >= 0 and right_subsequence[right_index] == right_subsequence_sum:
                right_count += 1
                right_index -= 1

            answer += left_count * right_count

        elif left_subsequence_sum + right_subsequence_sum > S:
            right_index -= 1
        else:
            left_index += 1

    if S == 0:
        answer -= 1

    return answer


def solution():
    N, S = map(int, input().split())
    sequence = list(map(int, input().split()))

    left_subsequence = []
    right_subsequence = []

    subsequence_sum(0, 0, N//2, sequence, left_subsequence)
    subsequence_sum(0, N//2, N, sequence, right_subsequence)
    left_subsequence.sort()
    right_subsequence.sort()

    answer = two_pointer(left_subsequence, right_subsequence, S)
    print(answer)


solution()

