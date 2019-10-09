from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *


class QDMGraphicsView(QGraphicsView):
    """description of class"""
    def __init__(self, scene, parent=None):
        super().__init__(parent)
        self.grScene = scene

        self.initUI()

        self.setScene(self.grScene)

        self.zoomFactor = 1.25
        self.zoomClamp = False
        self.zoom = 10
        self.zoomStep = 1
        self.zoomRange = [0, 10]

    def initUI(self):
        self.setRenderHints(QPainter.Antialiasing | QPainter.HighQualityAntialiasing | QPainter.TextAntialiasing | QPainter.SmoothPixmapTransform)
        self.setViewportUpdateMode(QGraphicsView.FullViewportUpdate)
        self.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.setTransformationAnchor(QGraphicsView.AnchorUnderMouse)

    def mousePressEvent(self, event):
        if event.button() == Qt.MiddleButton:
            self.middleMouseButtonPress(event)
        elif event.button() == Qt.LeftButton:
            self.leftMouseButtonPress(event)
        elif event.button() == Qt.RightButton:
            self.rightMouseButtonPress(event)
        else:
            super().mousePressEvent(event)

    def mouseReleaseEvent(self, event):
        if event.button() == Qt.MiddleButton:
            self.middleMouseButtonRelease(event)
        elif event.button() == Qt.LeftButton:
            self.leftMouseButtonRelease(event)
        elif event.button() == Qt.RightButton:
            self.rightMouseButtonRelease(event)
        else:
            super().mouseReleaseEvent(event)

    def middleMouseButtonPress(self, event):
        releaseEvent = QMouseEvent(QEvent.MouseButtonRelease, event.localPos(), event.screenPos(),
                                   Qt.LeftButton, Qt.NoButton, event.modifiers())
        super().mouseReleaseEvent(releaseEvent)
        self.setDragMode(QGraphicsView.ScrollHandDrag)
        pressEvent = QMouseEvent(event.type(), event.localPos(), event.screenPos(),
                                 Qt.LeftButton, event.buttons() | Qt.LeftButton, event.modifiers())
        super().mousePressEvent(pressEvent)

    def middleMouseButtonRelease(self, event):
        releaseEvent = QMouseEvent(event.type(), event.localPos(), event.screenPos(),
                                   Qt.LeftButton, event.buttons() & ~Qt.LeftButton, event.modifiers()) # Need to & ~lbutton to process proper actual state of left mouse button
        super().mouseReleaseEvent(releaseEvent)
        self.setDragMode(QGraphicsView.NoDrag)

    def leftMouseButtonPress(self, event):
        return super().mousePressEvent(event)

    def rightMouseButtonPress(self, event):
        return super().mousePressEvent(event)

    def leftMouseButtonRelease(self, event):
        return super().mousePressEvent(event)

    def rightMouseButtonRelease(self, event):
        return super().mousePressEvent(event)

    def wheelEvent(self, event):
        # calculate zoom factor
        zoomOutFactor = 1 / self.zoomFactor

        # calculate zoom
        if event.angleDelta().y() > 0:
            zoomFactor = self.zoomFactor
            self.zoom += self.zoomStep
        else:
            zoomFactor = zoomOutFactor
            self.zoom -= self.zoomStep

        # set scene scale
        self.scale(zoomFactor, zoomFactor)

        # translate view
        # return super().wheelEvent(event)