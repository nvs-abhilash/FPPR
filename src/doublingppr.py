import numpy as np
from doubling import Doubling


def Geom(epsilon, R):
    return list(np.random.geometric(p=epsilon, size=R+1))


def ChooseTheta(G, lam_vector):
    R = len(lam_vector)
    theta = [3 for i in range(0, R+1)]
    return theta


def DoublingPPR(G, L, epsilon):

    R = int(epsilon * L)
    V = G.getVertices()
    
    lam_vector = Geom(epsilon, R)
    theta = ChooseTheta(G, lam_vector)

    W = {}
    for i in range(1, R+1):
        W[i] = Doubling(G, lam_vector[i], theta[i])

    C = {}
    for u in V:
        C[u] = {}

    for u in V:
        for v in V:
            C[u][v] = 0

    for i in range(1, R+1):
        for u in V:
            for v in V:
                cnt = 0
                for x in W[i][u]:
                    if x == v:
                        cnt += 1
                C[u][v] += cnt

    lam_sum = sum(lam_vector)
    pi = {}
    for u in V:
        pi[u] = {}

    for u in V:
        for v in V:
            pi[u][v] = C[u][v] / lam_sum

    return pi
