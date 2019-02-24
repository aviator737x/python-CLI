from skbio.util._decorator import overrides


class CommandInterface(object):
    def __init__(self, stream, *args):
        self.arguments = args
        self.stream = stream

    def main_method(self, *args):
        pass

    def evaluate(self):
        print(self.main_method(self.arguments), file=self.stream)

    def get_stream(self, stream):
        self.stream = stream

    def pass_stream(self):
        pass


class Cat(CommandInterface):
    @overrides
    def main_method(self, path):
        with open(path, 'r') as input_file


def echo(args=None):
    pass


def wc(path):
    pass


def pwd():
    pass


def apply(cmd, *args, **kwargs):
    pass
