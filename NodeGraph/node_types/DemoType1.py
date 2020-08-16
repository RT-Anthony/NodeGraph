from collections import OrderedDict

from Node import Node
from NodeSerializable import Serializable
from PyQt5.QtWidgets import *

class DemoType1(Node):
    def __init__(self, scene, title="DemoAdd"):
        content = DemoContent(self)
        super().__init__(scene, title, [1, 1], [4], content, height=100)


class DemoContent(QWidget, Serializable):
    def __init__(self, node, parent=None):
        self.node = node
        super().__init__(parent=None)

        self.initUI()

    def initUI(self):
        self.layout = QVBoxLayout()
        self.layout.setContentsMargins(0, 0, 0, 0)
        self.setLayout(self.layout)
        #self.layout.addWidget(self.wdg_label)
        self.layout.addWidget(QLineEdit("foo"))

    def serialize(self):
        return OrderedDict([
            
            ])

    def deserialize(self, data, hashmap={}):
        return False
