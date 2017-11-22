import math
from genseg import GenSeg

def Doubling(G, lam, theta):
    S = GenSeg(G, lam, theta)
    V = G.getVertices()
    eta = math.ceil(lam / theta)


    W = {}
    E = {}
    for u in V:
        W[u] = [{} for i in range(0, eta+1)]
        E[u] = [{} for i in range(0, eta+1)]

    for u in V:
        for i in range(1, eta+1):
            W[u][i][eta] = S[u][i]
            E[u][i][eta] = S[u][i][-1]

    while eta > 1:
        eta_dash = (eta + 1) // 2

        for i in range(1, eta_dash+1):
            for u in V:
                if i == (eta+1)/2:
                    W[u][i][eta_dash] = W[u][i][eta]
                    E[u][i][eta_dash] = E[u][i][eta]

                v = E[u][i][eta]
                W[u][i][eta_dash] = W[u][i][eta]
                W[u][i][eta_dash].extend(W[v][eta-i+1][eta][1:])
                E[u][i][eta_dash] = E[v][eta - i + 1][eta]

        eta = eta_dash

    final_walk = {}
    for u in V:
        final_walk[u] = W[u][1][1]

    return final_walk
