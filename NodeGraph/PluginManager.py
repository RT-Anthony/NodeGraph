import importlib


class Plugin(object):
    """
    Base plugin class to inherit from
    """
    def __init__(self):
        raise NotImplementedError

    def execute(self):
        raise NotImplementedError


class PluginManager(object):
    """
    Manages plugins and how they are loaded
    """
    def __init__(self):
        pass

    def refresh(self):
        pass
