from Report import Plugin
from dot_Plugin import Plugin_to_dot

class app(Plugin):
    METHODS = ['create_app']
    def __init__(self):
        pass


    def _get_graph(self,Report):


        self.graph = {}
        self.nodes = []

    def create_app(self,Report):
        from flask import Flask

        app = Flask(__name__)
        class meta:
            def __init__(self,node,parser):
                self.__name__ = 'n_%s'%node.id_node
                self.node = node
                self.parser = parser

            def __call__(self):
                return self.parser('',self.node.run())

        for n in Report.nodes:
            f = meta(n,self.parser)
            app.route('/'+f.__name__)(f)

        @app.route('/')
        def index():
            import pydot
            return  pydot.graph_from_dot_data(Plugin_to_dot().to_dot(index.Report))[0].create_svg()
        index.Report = Report
        self.app = app
        return app

    def parser(self,type,ans):
        return str(ans)

