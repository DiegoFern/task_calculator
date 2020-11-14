from nodes import Node
from Report import Plugin

class PandaPlugin(Plugin):
    FACTORY = [
        'charge_xlsx',
        'charge_csv',
    ]
    import pandas as pd
    METHODS =[
        'set_directory',
        'get_directory',
    ]

    def set_directory(self,Report,directory):
        self.directory = directory

    def get_directory(self,Report):
        return self.directory

    def set_directory_out(self,Report,directory):
        self.directory_out = directory

    def get_directory_out(self,Report):
        return self.directory_out


    def charge_csv(self,Report,nameFile,**args):
        def f():
            return f.self.pd.read_csv(
                f.self.directory+nameFile,**args
            )
        f.self = self
        f.nameFile = nameFile
        f.__name__ = 'charge_csv{}'.format(nameFile)
        return f


    def charge_xlsx(self,Report,nameFile,**args):
        def f():
            return f.self.pd.read_excel(
                f.self.directory+nameFile,**args
            )
        f.self = self
        f.nameFile = nameFile
        f.__name__ = 'charge_xlsx_{}'.format(nameFile)
        return f

    def to_csv(self,Report,nameFile,**args):
        def f():
            return f.self.pd.to_csv(
                f.self.directory_out+nameFile,**args
            )
        f.self = self
        f.nameFile = nameFile
        f.__name__ = 'to_csv{}'.format(nameFile)
        return f

