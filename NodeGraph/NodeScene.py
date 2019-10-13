from NodeGraphicsScene import NodeGraphicsScene
class NodeScene(object):
    """description of class"""

    def __init__(self):
        self.nodes = []
        self.edges = []

        self.scene_width = 64000
        self.scene_height = 64000

        self.initUI()

    def initUI(self):
        self.grScene = NodeGraphicsScene(self)
        self.grScene.setGrScene(self.scene_width, self.scene_height)

    def addNode(self, node):
        self.nodes.append(node)

    def addEdge(self, edge):
        self.edges.append(edge)

    def removeNode(node):
        self.nodes.remove(node)

    def removeEdge(edge):
        self.edges.remove(edge)
