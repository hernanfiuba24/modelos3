import pygraphviz as pgv


class Graph:
    def __init__(self, df, isDirected):
        self.G = pgv.AGraph(directed=isDirected)
        self.df = df
        for row in df.itertuples(index=False):
            # label = '/'.join(row.name)
            label = "P-" + row.id
            self.G.add_node(row.id)
            for node in row.adyacents:
                self.G.add_edge(int(row.id), node)

    def write(self, file_name):
        self.G.write("../output/" + file_name + ".dot")

    def draw(self, file_name):
        self.G.graph_attr['label'] = file_name
        self.G.graph_attr['imagescale'] = True
        self.G.graph_attr['splines'] = 'line'
        # self.G.graph_attr['overlap'] = False
        # self.G.graph_attr['splines'] = True
        # self.G.graph_attr['wight'] = 2400
        # self.G.graph_attr['hight'] = 1600
        self.G.graph_attr['nodesep'] = 1.5

        self.G.node_attr['style'] = 'rounded'
        self.G.node_attr['shape'] = 'rect'
        self.G.node_attr['penwidth'] = 0.1
        # self.G.node_attr['fixsize'] = True

        self.G.edge_attr['color'] = 'black'
        self.G.edge_attr['penwidth'] = 2
        # self.G.edge_attr['arrowhead'] = 'normal'
        # self.G.edge_attr['arrowsize'] = 10.0
        # self.G.edge_attr['arrowtype'] = 10
        self.G.layout()
        self.G.draw("output/" + file_name + ".png")

    def draw(self, file_name, bestPath):
        self.G.graph_attr['label'] = file_name
        self.G.graph_attr['imagescale'] = True
        self.G.graph_attr['splines'] = 'line'
        self.G.graph_attr['nodesep'] = 1.5

        self.G.node_attr['style'] = 'rounded'
        self.G.node_attr['shape'] = 'rect'
        self.G.node_attr['penwidth'] = 0.1

        self.G.edge_attr['color'] = 'black'
        self.G.edge_attr['penwidth'] = 2

        for node in bestPath:
            node = self.G.get_node(node)
            node.attr['color'] = 'red'
            node.attr['penwidth'] = 0.5
        for i in range(len(bestPath)-1):
            edge = self.G.get_edge(bestPath[i], bestPath[i+1])
            edge.attr['color'] = 'red'

        self.G.layout()
        self.G.draw("./output/" + file_name + ".png")

    def neighbors_iter(self, node, funcion, args):
        for nodeAdyacent in self.G.neighbors_iter(node):
            edge = [node, nodeAdyacent]
            args = funcion(edge, args)
        return args
