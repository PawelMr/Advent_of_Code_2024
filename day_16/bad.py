def aoc16():
    from heapq import heappop, heappush

    M = {c + 1j * r: v for r, l in enumerate(open("input.txt")) for c, v in enumerate(l.strip())}
    start = next(k for k, v in M.items() if v == "S")
    end = next(k for k, v in M.items() if v == "E")

    def dijkstra(origin, k=1):  # k=1 to go forwards, k=-1 to go backwards
        G = {(p, d): {(p, d * 1j): 1000, (p, d * -1j): 1000} | ({(p + k * d, d): 1} if M[p + k * d] != "#" else {})
             for p, v in M.items() for d in [1, -1, 1j, -1j] if v != "#"}
        if k == -1: G |= {origin: {(origin[0], d): 0} for d in [1, -1, 1j, -1j]}  # hack
        # Garden variety Dijkstra algorithm
        D, V, Q = {}, set(), [(0, (s := 0, origin))]
        while Q:
            d, (_, v) = heappop(Q)
            if v not in V:
                V.add(v)
                for n, w in G[v].items():
                    if n not in D or d + w < D[n]:
                        D[n] = d + w
                        heappush(Q, (d + w, (s := s + 1, n)))
        return D

    # part 1
    D = dijkstra((start, 1))
    minscore = min(v for ((p, d), v) in D.items() if p == end)
    print(minscore)

    # part 2: Dijkstra in reverse
    E = dijkstra((end, 0), -1)
    print(len({p for ((p, d), v) in D.items() if v + E[(p, d)] == minscore}))

aoc16()