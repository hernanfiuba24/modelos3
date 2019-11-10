import pandas as pd
from graph import Graph
from grasp import *
import os


def main():
    graphName = "supermarket"
    df_hallways = readGraph("files/hallways.json", {"id": str, "names": list})
    df_adyacents = readGraph("files/hallwaysGraph.json",
                             {"id": str, "adyacents": list})
    df_adyacents = addColumnToDataFragment(df_adyacents, "name", df_hallways["names"].values)
    G = Graph(df_adyacents, False)

    # find the path by metaheuristic method (GRASP)
    sources = [0, 1]
    target = 13
    grasp = Grasp(sources, G)

    print("the best path to go " + str(target) + " is " + str(grasp.bestPathTo(target)[1]) + ". The cost is : " + str(grasp.bestPathTo(target)[0]))

    G.write(graphName)
    G.draw(graphName)

def addColumnToDataFragment(df, name, column):
    df[name] = column
    return df

def readGraph(file_name, dTypes):
    # more options can be specified also
    with pd.option_context('display.max_rows', None, 'display.max_columns', None):
        basePath = os.path.dirname(os.path.abspath(__file__))
        df = pd.read_json(basePath + '/' + file_name,
                          orient='hallways', dtype=dTypes)
        return df


if __name__ == "__main__":
    main()
