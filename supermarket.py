import pandas as pd
import os
from digraph import Digraph


def main():
    graphName = "supermarket"
    df_hallways = readGraph("files/hallways.json", {"id": str, "names": list})
    df_adyacents = readGraph("files/hallwaysDigraph.json",
                             {"id": str, "adyacents": list})
    df_adyacents = addColumnToDataFragment(df_adyacents, "name", df_hallways["names"].values)
    G = Digraph(df_adyacents, False)
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
