import pandas as pd
from graph import Graph
from grasp import *
import os


def main():
    hallwaysPathName = sys.argv[1]
    hallwaysGraphPathName = sys.argv[2]
    df_hallways = readGraph(hallwaysPathName, {"id": str, "names": list})
    df_adyacents = readGraph(hallwaysGraphPathName,
                             {"id": str, "adyacents": list})
    df_adyacents = addColumnToDataFragment(
        df_adyacents, "name", df_hallways["names"].values)
    G = Graph(df_adyacents, False)

    # find the path by metaheuristic method (GRASP)
    sources = [0, 1] # doors
    target = int(sys.argv[3])
    grasp = Grasp(sources, G)
    bestPath = grasp.bestPathTo(target)[1]
    bestCost = grasp.bestPathTo(target)[0]
    print("the best path to go " + str(target) + " is " +
          str(bestPath) + ". The cost is : " + str(bestCost))
    

    sourcesTocash = [21, 22] # cashbox
    targetToCash = int(target)
    graspToCash = Grasp(sourcesTocash, G)
    bestPathToCash = graspToCash.bestPathTo(targetToCash)[1]
    bestCostToCash = graspToCash.bestPathTo(targetToCash)[0]
    print("the best path to go " + str(targetToCash) + " is " +
          str(bestPathToCash) + ". The cost is : " + str(bestCostToCash))


    graphName = sys.argv[4]
    G.write(graphName)
    G.draw(graphName, bestPath, bestPathToCash)

def superMarketRoute(target, hallwaysName, hallwaysGraphName, sourcesTocash):
    basePath = os.path.abspath(os.path.join(__file__, '..', '..', 'files'))
    hallwaysPathName = basePath + '/' + hallwaysName + '.json'
    hallwaysGraphPathName = basePath + '/' + hallwaysGraphName + '.json'
    df_hallways = readGraph(hallwaysPathName, {"id": str, "names": list})
    df_adyacents = readGraph(hallwaysGraphPathName,
                             {"id": str, "adyacents": list})
    df_adyacents = addColumnToDataFragment(
        df_adyacents, "name", df_hallways["names"].values)
    G = Graph(df_adyacents, False)

    # find the path by metaheuristic method (GRASP)
    sources = [0, 1] # doors

    grasp = Grasp(sources, G)
    bestPath = grasp.bestPathTo(target)[1]
    bestCost = grasp.bestPathTo(target)[0]
    print("the best path to go " + str(target) + " is " +
          str(bestPath) + ". The cost is : " + str(bestCost))
    
    targetToCash = int(target)
    graspToCash = Grasp(sourcesTocash, G)
    bestPathToCash = graspToCash.bestPathTo(targetToCash)[1]
    bestCostToCash = graspToCash.bestPathTo(targetToCash)[0]
    print("the best path to go to the cash is " +
          str(bestPathToCash) + ". The cost is : " + str(bestCostToCash))

    G.write(hallwaysName)
    G.draw(hallwaysName, bestPath, bestPathToCash)

def hallwaysSuper(hallwaysName, hallwaysGraphName):
    basePath = os.path.abspath(os.path.join(__file__, '..', '..', 'files'))
    hallwaysPathName = basePath + '/' + hallwaysName + '.json'
    hallwaysGraphPathName = basePath + '/' + hallwaysGraphName + '.json'
    df_hallways = readGraph(hallwaysPathName, {"id": str, "names": list})
    df_adyacents = readGraph(hallwaysGraphPathName,
                             {"id": str, "adyacents": list})
    df_adyacents = addColumnToDataFragment(
        df_adyacents, "name", df_hallways["names"].values)
    G = Graph(df_adyacents, False)
    G.draw(hallwaysName, [], [])
    
def addColumnToDataFragment(df, name, column):
    df[name] = column
    return df


def readGraph(file_name, dTypes):
    # more options can be specified also
    with pd.option_context('display.max_rows', None, 'display.max_columns', None):
        df = pd.read_json(file_name,
                          orient='hallways', dtype=dTypes)
        return df


if __name__ == "__main__":
    main()
