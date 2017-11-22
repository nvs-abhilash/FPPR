""" A Python Class
A simple Python graph class, demonstrating the essential
facts and functionalities of graphs.
"""
import pandas as pd

class Graph(object):

    def __init__(self, fileName):
        df = pd.read_csv(fileName)

        self.graph_dict = {}
        self.col_names = []
        for col in df:
            self.col_names.append(col)

        rows = len(df)
        for i in range(0, rows):
            if df[self.col_names[1]][i] not in self.graph_dict.keys():
                self.graph_dict[df[self.col_names[1]][i]] = []

            try:
                self.graph_dict[df[self.col_names[0]][i]].append(df[self.col_names[1]][i])
            except:
                self.graph_dict[df[self.col_names[0]][i]] = [df[self.col_names[1]][i]]


    def getVertices(self):
        return self.graph_dict.keys()


    def getAdjList(self, u):
        try:
            return self.graph_dict[u]
        except:
            return None
