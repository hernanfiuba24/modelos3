import pygraphviz as pgv


class Digraph:
    def __init__(self, df):
        self.G = pgv.AGraph(directed=True)
        self.df = df
        for row in df.itertuples(index=False):
            label = "Label #" + str(row.id)
            self.G.add_node(row.id, label=label)
            for node in row.adyacents:
                self.G.add_edge(row.id, node)

    def write(self, file_name):
        self.G.write("output/" + file_name + ".dot")

    def draw(self, file_name):

        self.G.graph_attr['label'] = file_name
        self.G.node_attr['shape'] = 'oval'
        self.G.edge_attr['color'] = 'green'
        self.G.layout()
        self.G.draw("output/" + file_name + ".png")