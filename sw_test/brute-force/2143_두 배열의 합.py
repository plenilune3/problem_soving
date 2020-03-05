# def subsequence_sum(sum, index, length, sequence, result):
#     if index == length:
#         result.append(sum)
#     else:
#         subsequence_sum(sum, index+1, length, sequence, result)
#         subsequence_sum(sum+sequence[index], index+1, length, sequence, result)


def two_pointer(subsequence_A, subsequence_B, T):
    A_length = len(subsequence_A)
    A_index = 0
    B_index = len(subsequence_B) - 1
    answer = 0

    while A_index < A_length and B_index >= 0:
        A_value = subsequence_A[A_index]
        B_value = subsequence_B[B_index]

        if A_value + B_value == T:
            A_count = 0
            B_count = 0

            while A_index < A_length and subsequence_A[A_index] == A_value:
                A_count += 1
                A_index += 1
            while B_index >= 0 and subsequence_B[B_index] == B_value:
                B_count += 1
                B_index -= 1

            answer += A_count * B_count

        elif A_value + B_value > T:
            B_index -= 1
        else:
            A_index += 1

    return answer


def solution():
    T = int(input())
    N = int(input())
    A = list(map(int, input().split()))
    M = int(input())
    B = list(map(int, input().split()))

    subsequence_A = []
    subsequence_B = []

    for i in range(N):
        sum_A = A[i]
        subsequence_A.append(sum_A)
        for j in range(i+1, N):
            sum_A += A[j]
            subsequence_A.append(sum_A)
    for i in range(M):
        sum_B = B[i]
        subsequence_B.append(sum_B)
        for j in range(i+1, M):
            sum_B += B[j]
            subsequence_B.append(sum_B)

    subsequence_A.sort()
    subsequence_B.sort()
    answer = two_pointer(subsequence_A, subsequence_B, T)
    print(answer)


solution()
