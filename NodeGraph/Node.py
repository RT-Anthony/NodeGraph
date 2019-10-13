from QDMGraphicsNode import QDMGraphicsNode

class Node(object):
    """description of class"""
    def __init__(self, scene, title="Undefined Node"):
        self.scene = scene
        self.title = title

        self.grNode = QDMGraphicsNode(self, title)

        self.scene.addNode(self)
        self.scene.grScene.addItem(self.grNode)

        self.inputs = []
        self.outputs = []


