from nodes import Node
from functools import partial
class Plugin:
    METHODS = []
    FACTORIES_NODES = []
    def apply2Nodes(self,Node)->None:
        pass
    def __init__(self):
        pass
    def example_factories_node(self,*args,**kwargs)->Node:
        pass

class Report:
    def __init__(self):
        self.nodes = []
        self.PLUGINS = []
        self.nodes_dict = {}

    def new_node(self,**kwargs):
        node = Node(**kwargs)
        self.nodes.append(node)
        for plugin in (self.PLUGINS[:]):
            plugin.apply2Nodes(node)
        self.nodes_dict[node.id_node] = node
        return node.setfunction
    
    def __getitem__(self,n):
        return self.nodes_dict[n]

    def set_plugin(self,Plugin:Plugin,alias=None):
        for n in self.nodes:
            Plugin.apply2Nodes(n)

        if alias is None:
            alias=Plugin.__class__.__name__

        added_plugin = _Plugin()
        for method in Plugin.METHODS:
            setattr(added_plugin,method,partial(getattr(Plugin,method),self),)
        for method in Plugin.FACTORIES_NODES:
            def f(*args,**kwargs):
                node = f.attr(*args,**kwargs)
                f.self.nodes.append(node)
                f.self.nodes_dict[node.id_node] = (node)
                return node
             
            f.attr = getattr(Plugin,method)
            f.self = self
            setattr(added_plugin,method,(f))
        setattr(self,alias,added_plugin,)
        self.PLUGINS.append(Plugin)



class _Plugin:
    pass


