from skbio.util._decorator import overrides
import os


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
        with open(path, 'r') as input_file:
            result = ''
            for line in input_file:
                result += line
        return result


class Echo(CommandInterface):
    @overrides
    def main_method(self, *args):
        return args


class Wc(CommandInterface):
    @overrides
    def main_method(self, *args):
        result = []
        for path in args:
            result.append({'line': 0, 'word': 0, 'byte': 0, 'file': path})
            with open(path, 'r') as f:
                for line in f:
                    result[-1]['line'] += 1
                    result[-1]['word'] += len(line.split())
            with open(path, 'rb') as f:
                for line in f:
                    result[-1]['byte'] += len(line)
        string_result = ''
        for res in result:
            string_result += \
                '  {}  {}  {}  {}\n'.format(
                    res['line'],
                    res['word'],
                    res['byte'],
                    res['file'])

        return string_result


class Pwd(CommandInterface):
    @overrides
    def main_method(self):
        return os.getcwd()


class Ls(CommandInterface):
    @overrides
    def main_method(self, *args):
        """Prints list of files and folders of given directory or of current directory if no arguments given"""
        command = list(args)
        if len(command) > 3:
            return "ls takes zero or one parameter"
        else:
            if len(command) == 1 or len(command) == 2:
                res = os.listdir(os.getcwd())
                s = ""
                for folder in res:
                    s += folder + "\n"
                return s
            else:
                res = os.listdir(command[2])
                s = ""
                for folder in res:
                    s += folder + "\n"
                return s


class Cd(CommandInterface):
    @overrides
    def main_method(self, *args):
        """Changes directory to given or doesn't change anything if no arguments given"""
        command = list(args)
        if len(command) > 3:
            return "ls takes zero or one parameter"
        else:
            if len(command) == 1 or len(command) == 2:
                os.chdir(os.getcwd())
            else:
                os.chdir(command[2])
