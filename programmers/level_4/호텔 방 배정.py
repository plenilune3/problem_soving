from sys import setrecursionlimit

setrecursionlimit(10 ** 6)


class UnionFind:
    def __init__(self, room_number):
        self.parents = {x: x for x in set(room_number)}
        self.rank = {key: 0 for key in self.parents}

    def find(self, u):
        if u not in self.parents:
            self.parents[u] = u
            self.rank[u] = 0

        if u == self.parents[u]:
            return u
        else:
            self.parents[u] = self.find(self.parents[u])
            return self.parents[u]

    def union(self, u, v):
        u = self.find(u)
        v = self.find(v)

        if u == v:
            return

        if self.rank[u] > self.rank[v]:
            u, v = v, u

        self.parents[u] = v

        if self.rank[u] == self.rank[v]:
            self.rank[u] += 1


def solution(k, room_number):
    answer = []

    u = UnionFind(room_number)

    for requested in room_number:
        assigned = u.find(requested)
        u.union(requested, assigned + 1)
        answer.append(assigned)

    return answer
