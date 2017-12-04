"""
Given u, v -> (node, adjacency list)
"""
import sys


def main():
    graph_dict = {}

    for line in sys.stdin:
        u, v, w, t = line.strip().split(",")

        try:
            graph_dict[u].append(v)
        except:
            graph_dict[u] = [v]

    for key in graph_dict.keys():
        sys.stdout.write(key)
        if len(graph_dict[key]) > 0:
            sys.stdout.write(',')

        cnt = 0
        for val in graph_dict[key]:
            sys.stdout.write(val)
            cnt += 1
            if cnt != len(graph_dict[key]):
                sys.stdout.write(',')

        sys.stdout.write("\n")


if __name__ == '__main__':
    main()
