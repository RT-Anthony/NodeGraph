from QDMGraphicsNode import QDMGraphicsNode
from QDMNodeContentWidget import QDMNodeContentWidget

class Node(object):
    """description of class"""
    def __init__(self, scene, title="Undefined Node"):
        self.scene = scene
        self.title = title

        self.content = QDMNodeContentWidget()
        self.grNode = QDMGraphicsNode(self)

        self.scene.addNode(self)
        self.scene.grScene.addItem(self.grNode)

        self.inputs = []
        self.outputs = []


