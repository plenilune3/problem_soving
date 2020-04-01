def solution(budgets, M):
    answer = 0
    budget_min, budget_max = 0, max(budgets)

    while budget_min <= budget_max:
        budget_mid = (budget_min + budget_max) // 2
        temp = [budget if budget < budget_mid else budget_mid for budget in budgets]

        if sum(temp) > M:
            budget_max = budget_mid - 1
        else:
            answer = budget_mid
            budget_min = budget_mid + 1

    return answer
