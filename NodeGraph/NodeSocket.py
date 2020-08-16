from collections import OrderedDict
from enum import Enum
from NodeSerializable import Serializable
from QNGGraphicsSocket import QNGGraphicsSocket


class SocketLocation(Enum):
   INPUT_TOP = 1
   INPUT_BOTTOM = 2
   OUTPUT_TOP = 3
   OUTPUT_BOTTOM = 4


class SocketType(Enum):
    INPUT = 1
    OUTPUT = 2


DEBUG = False


class Socket(Serializable):
    def __init__(self, node, index=0, position=SocketLocation.INPUT_TOP, socket_color=1, socket_type=SocketType.INPUT):
        super().__init__()
        self.node = node
        self.index = index
        self.position = position
        self.socket_color = socket_color

        if DEBUG: print("Socket -- creating with", self.index, self.position, "for node", self.node)


        self.grSocket = QNGGraphicsSocket(self, self.socket_color)

        self.grSocket.setPos(*self.node.getSocketPosition(index, position))

        self.edge = None

    def __str__(self):
        return "<Socket %s..%s>" % (hex(id(self))[2:5], hex(id(self))[-3:])


    def getSocketPosition(self):
        if DEBUG: print("  GSP: ", self.index, self.position, "node:", self.node)
        res = self.node.getSocketPosition(self.index, self.position)
        if DEBUG: print("  res", res)
        return res


    def setConnectedEdge(self, edge=None):
        self.edge = edge

    def getConnectedEdge(self):
        return self.edge

    def hasEdge(self):
        return self.edge is not None

    def serialize(self):
        return OrderedDict([
            ('id', self.id),
            ('index', self.index),
            ('position', self.position),
            ('socket_color', self.socket_color),
        ])

    def deserialize(self, data, hashmap={}):
        self.id = data['id']
        hashmap[data['id']] = self
        return True
