from nodes import Node
from functools import partial
class Plugin:
    METHODS = []
    def apply2Nodes(self,Node)->None:
        pass
    def __init__(self):
        pass

class Report:
    def __init__(self):
        self.nodes = []
        self.PLUGINS = []

    def new_node(self,**kwargs):
        node = Node(**kwargs)
        self.nodes.append(node)
        for plugin in (self.PLUGINS[:]):
            plugin.apply2Nodes(node)
        return node.setfunction

    def set_plugin(self,Plugin:Plugin,alias=None):
        for n in self.nodes:
            Plugin().apply2Nodes(n)

        if alias is None:
            alias=Plugin.__name__

        added_plugin = _Plugin()
        for method in Plugin.METHODS:
            setattr(added_plugin,method,partial(getattr(Plugin,method),self),)
        setattr(self,alias,added_plugin,)




class _Plugin:
    pass


