from collections import OrderedDict
from NodeSerializable import Serializable
from QNGGraphicsNode import QNGGraphicsNode
from QNGNodeContentWidget import QNGNodeContentWidget
from NodeSocket import *

DEBUG = False

class Node(Serializable):
    """description of class"""
    def __init__(self, scene, title="Undefined Node", inputs=None, outputs=None, content=None, width=180, height=240):
        super().__init__()
        self._title = title
        self.scene = scene

        if content: 
            self.content = content
        else: 
            self.content = QNGNodeContentWidget(self)
        self.grNode = QNGGraphicsNode(self, None, width, height)
        self.title = title

        self.scene.addNode(self)
        self.scene.grScene.addItem(self.grNode)

        self.socket_spacing = 22

        # create socket for inputs and outputs
        self.inputs = []
        self.outputs = []
        counter = 0
        if inputs is not None:
            for item in inputs:
                socket = InputSocket(node=self, index=counter, position=SocketLocation.INPUT_BOTTOM, socket_color=item)
                counter += 1
                self.inputs.append(socket)

        if outputs is not None:
            counter = 0
            for item in outputs:
                socket = OutputSocket(node=self, index=counter, position=SocketLocation.OUTPUT_TOP, socket_color=item)
                counter += 1
                self.outputs.append(socket)

    def __str__(self):
        return "<Node %s..%s>" % (hex(id(self))[2:5], hex(id(self))[-3:])

    @property
    def pos(self):
        return self.grNode.pos()        # QPointF

    def setPos(self, x, y):
        self.grNode.setPos(x, y)

    @property
    def title(self): return self._title

    @title.setter
    def title(self, value):
        self._title = value
        self.grNode.title = self._title

    def getSocketPosition(self, index, position):
        x = 0 if (position in (SocketLocation.INPUT_TOP, SocketLocation.INPUT_BOTTOM)) else self.grNode.width

        if position in (SocketLocation.INPUT_BOTTOM, SocketLocation.OUTPUT_BOTTOM):
            # start from bottom
            y = self.grNode.height - self.grNode.edge_size - self.grNode._padding - index * self.socket_spacing
        else :
            # start from top
            y = self.grNode.title_height + self.grNode._padding + self.grNode.edge_size + index * self.socket_spacing

        return [x, y]


    def updateConnectedEdges(self):
        for socket in self.inputs:
            if socket.hasEdge():
                socket.edge.updatePositions()

        for socket in self.outputs:
            if socket.hasEdge():
                for edge in socket.getConnectedEdges():
                    edge.updatePositions()


    def remove(self):
        if DEBUG: print("> Removing Node", self)
        if DEBUG: print(" - remove all edges from sockets")
        for socket in (self.inputs):
            if socket.hasEdge():
                if DEBUG: print("    - removing from socket:", socket, "edge:", socket.edge)
                socket.edge.remove()
        for socket in (self.outputs):
            if socket.hasEdge():
                if DEBUG: print("    - removing from socket:", socket, "edge:", socket.edge)
                socket.edge.remove()
        if DEBUG: print(" - remove grNode")
        self.scene.grScene.removeItem(self.grNode)
        self.grNode = None
        if DEBUG: print(" - remove node from the scene")
        self.scene.removeNode(self)
        if DEBUG: print(" - everything was done.")

    def serialize(self):
        inputs, outputs = [], []
        for socket in self.inputs: inputs.append(socket.serialize())
        for socket in self.outputs: outputs.append(socket.serialize())
        return OrderedDict([
            ('id', self.id),
            ('title', self.title),
            ('pos_x', self.grNode.scenePos().x()),
            ('pos_y', self.grNode.scenePos().y()),
            ('inputs', inputs),
            ('outputs', outputs),
            ('content', self.content.serialize()),
        ])

    def deserialize(self, data, hashmap={}):
        self.id = data['id']
        hashmap[data['id']] = self

        self.setPos(data['pos_x'], data['pos_y'])
        self.title = data['title']

        data['inputs'].sort(key=lambda socket: socket['index'] + socket['position'] * 10000 )
        data['outputs'].sort(key=lambda socket: socket['index'] + socket['position'] * 10000 )

        self.inputs = []
        for socket_data in data['inputs']:
            new_socket = Socket(node=self, index=socket_data['index'], position=socket_data['position'],
                                socket_color=socket_data['socket_type'])
            new_socket.deserialize(socket_data, hashmap)
            self.inputs.append(new_socket)

        self.outputs = []
        for socket_data in data['outputs']:
            new_socket = Socket(node=self, index=socket_data['index'], position=socket_data['position'],
                                socket_color=socket_data['socket_type'])
            new_socket.deserialize(socket_data, hashmap)
            self.outputs.append(new_socket)
        return True


