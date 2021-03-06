from nodes import Node
from functools import partial
class Plugin:
    METHODS = []
    FACTORY = []
    FACTORY_NO_SAVED = []
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

    def new_node(self,save=True,**kwargs):
        node = Node(save=save,**kwargs)
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
            setattr(
                added_plugin,
                method,
                partial(getattr(Plugin,method),self),
            )
        for factory in Plugin.FACTORY:
            def factory_function(*args,**kwargs):
                return factory_function.Report.new_node()(factory_function.method(*args,**kwargs))
            factory_function.Report = self
            factory_function.method =  partial(getattr(Plugin,factory),self)
            setattr(
                added_plugin,
                factory,
                factory_function
            )
        for factory in Plugin.FACTORY_NO_SAVED:
            def factory_function(*args,**kwargs):
                return factory_function.Report.new_node()(factory_function.method(*args,**kwargs))
            factory_function.Report = self
            factory_function.method =  partial(getattr(Plugin,factory),self)
            setattr(
                added_plugin,
                factory,
                factory_function
            )
        setattr(self,alias,added_plugin,)
        self.PLUGINS.append(Plugin)



class _Plugin:
    pass


