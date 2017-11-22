import math
import random
from datetime import datetime

def RandomNeighbour(u, G):
    random.seed(datetime.now())
    lst = G.getAdjList(u)
    v = math.floor(random.random() * len(lst))

    if len(lst) == 0:
        return None
    return lst[v]


def GenSeg(G, lam, theta):
    """
    """

    V = G.getVertices()
    number_of_segments = math.ceil(lam / theta)

    S = {}
    for u in V:
        S[u] = [[u] for i in range(0, number_of_segments+1)]

    for j in range(1, theta+1):
        for i in range(1, number_of_segments+1):
            if i == number_of_segments and 0 < (lam - theta*(lam//theta)) < j:
                break
            for u in V:
                w = RandomNeighbour(S[u][i][-1], G)
                if w is not None:
                    S[u][i].append(w)
    return S
