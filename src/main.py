from graph import Graph
from doublingppr import DoublingPPR
# from genseg import GenSeg
# from sqrt import Sqrt
# from doubling import Doubling

def main():
    G = Graph("../soc-sign-bitcoinalpha.csv")
    pi = DoublingPPR(G, 5, 0.2)
    V = G.getVertices()

    out_file = open('../out.csv', 'w')

    for u in V:
        for v in V:
            if pi[u][v] != 0:
                print('{0},{1},{2:.2f}'.format(u, v, float(pi[u][v])), file=out_file)
    
    # for u in V:
    #     print(u, end=': ')
    #     for v in V:
    #         print('{0:.2f}'.format(float(pi[u][v])), end=' ')
    #     print()

    # S = GenSeg(G, 18, 3)
    # W = Sqrt(G, 18, 3)
    # Doubling(G, 18, 3)

    # print("Matrix S: ")
    # for key in S.keys():
    #     print(key, S[key])

    # print("Matrix W(Sqrt): ")
    # for key in W.keys():
    #     print(key, W[key])



if __name__ == "__main__":
    main()
