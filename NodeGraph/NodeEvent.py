from enum import Enum

class EventType(Enum):
    KEYPRESS   = 0b00000001
    MOUSECLICK = 0b00000010
    COPY       = 0b00000100
    PASTE      = 0b00001000
    INSERT     = 0b00010000
    DELETE     = 0b00100000
    UPDATE     = 0b01000000
    NODE       = 0b10000000

class NodeEvent(object):
    """description of class"""
    def __init__(self, parent_node, event_type, action_callback, undo_callback):
        self._parent_node = parent_node
        self._event_type = event_type
        self._action_callback = action_callback
        self._undo_callback = undo_callback

    def execute(self, *args, **kwargs):
        return self._action_callback(args, kwargs)

    def undo(self, *args, **kwargs):
        return self._undo_callback(args, kwargs)

    def isType(event_type):
        return self._event_type & event_type
