import pandas as pd
import os

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