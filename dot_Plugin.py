from Report import Plugin
from nodes import Node

class Plugin_to_dot(Plugin):
    METHODS=['to_dot']

    def to_dot(self):
        print('digraph{')
        for node in self.nodes:
            print(Plugin_to_dot.print_node(node))
            for g in (Plugin_to_dot.print_edge(node)):
                print(g)
        print('}')



    def print_node(node):
        return ''' n_{n}[ shape=square, label='{f}' color={color},styled='filled' ]; '''.format(
                   f=str(node.function.__name__),
                   n=node.id_node,
                   color='green' if node.calculated else 'red'
            )

    def print_edge(node):
        for i in node.previous.values():
            if  issubclass(type(i), Node):
                yield ''' {n}->{m}; '''.format(n=i.id_node,
                                              m=node.id_node)





