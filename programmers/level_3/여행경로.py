answer = []


def dfs(depth, graph, tickets, node, result=None):
    global answer

    if result is None:
        result = [node]

    if answer:
        return
    elif not tickets:
        answer = result.copy()
    else:
        for node_next in graph[node]:
            if [node, node_next] in tickets:
                tickets.remove([node, node_next])
                result.append(node_next)
                dfs(depth + 1, graph, tickets, node_next, result)
                tickets.append([node, node_next])
                result.pop()


def solution(tickets):
    global answer
    graph = {}

    for ticket in tickets:
        A, B = ticket

        if graph.get(A) is None:
            graph[A] = [B]
        else:
            graph[A].append(B)

        if graph.get(B) is None:
            graph[B] = []

    for ticket in tickets:
        A, B = ticket
        graph[A].sort()

    dfs(0, graph, tickets, "ICN")

    return answer
