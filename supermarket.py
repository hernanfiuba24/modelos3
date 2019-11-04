import pandas as pd
import os
from digraph import Digraph

def main():
    graphName = "supermarket"
    readGraph("files/hallways.json", {"id": str, "names": list})
    df = readGraph("files/hallwaysDigraph.json", {"id": str, "adyacents": list})
    G = Digraph(df)
    G.write(graphName)
    G.draw(graphName)


def readGraph(file_name, dTypes):
    # more options can be specified also
    with pd.option_context('display.max_rows', None, 'display.max_columns', None):
        basePath = os.path.dirname(os.path.abspath(__file__))
        df = pd.read_json(basePath + '/' + file_name,
                          orient='hallways', dtype=dTypes)
        """
        df_ids = df.filter(items=["id"])
        print(file_name + " registers " + str(df_ids.size))
        print(df_ids)
        """
        return df


if __name__ == "__main__":
    main()
