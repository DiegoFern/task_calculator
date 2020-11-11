from typing import Dict,Any
from itertools import count

class Node:
    n_node = count()

    def __init__(self,**previous):
        self.previous = previous
        self.calculated = False
        def f(**kwargs):
            return
        self.function = f
        self._name = None
        self.id_node = next(self.n_node)

    def setfunction(self,f):
        self.function = f
        if self._name == None:
            self._name=f.__name__
        return self
    
    def setname(self,name):
        self._name=name

    def run(self):
        if self.calculated:
            return self.ans

        kwargs = {}
        for i in self.previous:
            node = self.previous[i]
            if issubclass(type(node),Node):
                kwargs[i] = node.run()
            else:
                kwargs[i] = node
        self.ans = self.function(**kwargs)
        self.calculated = True
        return self.ans


