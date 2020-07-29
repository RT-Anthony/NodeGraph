from enum import Enum

class EventType(Enum):
    KEYPRESS   = 0b0000001
    MOUSECLICK = 0b0000010
    COPY       = 0b0000100
    PASTE      = 0b0001000
    INSERT     = 0b0010000
    DELETE     = 0b0100000

class NodeEvent(object):
    """description of class"""
    def __init__(self, action_callback, undo_callback):
        self._action_callback = action_callback
        self._undo_callback = undo_callback

    def execute(self, *args, **kwargs):
        return self._action_callback(args, kwargs)

    def undo(self, *args, **kwargs):
        return self._undo_callback(args, kwargs)
