from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

from NodeScene import NodeScene
from QDMGraphicsView import QDMGraphicsView
from Node import Node

class NodeEditorWindow(QWidget):
    """description of class"""
    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.initUI()

    def initUI(self):
        self.setGeometry(200, 200, 800, 600)
        self.layout = QVBoxLayout()
        self.layout.setContentsMargins(0,0,0,0)
        self.setLayout(self.layout)
        
        # create graphics scene
        self.scene = NodeScene()
        
        node = Node(self.scene, "My Awesome Node")

        # create graphics view
        self.view = QDMGraphicsView(self.scene.grScene, self)
        self.layout.addWidget(self.view)

        self.setWindowTitle("Node Editor")
        self.show()

        # self.addDebugContent()

    def addDebugContent(self):
        greenBrush = QBrush(Qt.green)
        outlinePen = QPen(Qt.black)
        outlinePen.setWidth(2)
        rect = self.grScene.addRect(500, 500, 80, 100, outlinePen, greenBrush)
        rect.setFlag(QGraphicsItem.ItemIsMovable)

        text = self.grScene.addText("This is my awesome text!")
        text.setFlag(QGraphicsItem.ItemIsSelectable)
        text.setFlag(QGraphicsItem.ItemIsMovable)
        text.setDefaultTextColor(QColor.fromRgbF(1.0, 1.0, 1.0))

        widget1 = QPushButton("Hello World")
        proxy1 = self.grScene.addWidget(widget1)
        proxy1.setFlag(QGraphicsItem.ItemIsMovable)
        proxy1.setPos(30,30)

        # widget2 = QTextEdit()
        # proxy2 = self.grScene.addWidget(widget2)
        # proxy2.setFlag(QGraphicsItem.ItemIsSelectable)
        # proxy2. setPos(70, 30)
