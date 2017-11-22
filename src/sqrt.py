from genseg import GenSeg
import math

def Sqrt(G, lam, theta):
    S = GenSeg(G, lam, theta)
    V = G.getVertices()
    number_of_segments = math.ceil(lam / theta)

    W = {}
    for u in V:
        W[u] = [u]

    for i in range(1, number_of_segments+1):
        for u in V:
            W[u].extend(S[W[u][-1]][i][1:])
    return W
