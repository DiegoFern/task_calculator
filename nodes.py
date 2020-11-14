from typing import Dict,Any
from itertools import count

class Node:
    n_node = count()

    def __init__(self,save=True,**previous):
        self.previous = previous
        self.calculated = False
        def f(**kwargs):
            return
        self.function = f
        self._name = None
        self.id_node = next(self.n_node)
        self.save = save and all(map(lambda x:x.save,
            filter(lambda node:issubclass(type(node),Node),self.previous.values())))

    def setfunction(self,f):
        self.function = f
        if self._name == None:
            self._name=f.__name__
        return self
    
    def setname(self,name):
        self._name=name

    def run(self):
        if self.save and self.calculated:
            return self.ans

        kwargs = {}
        for i in self.previous:
            node = self.previous[i]
            if issubclass(type(node),Node):
                kwargs[i] = node.run()
            else:
                kwargs[i] = node
        if not self.save:
            return self.function(**kwargs)
        else:
            self.ans = self.function(**kwargs)
            return self.ans


