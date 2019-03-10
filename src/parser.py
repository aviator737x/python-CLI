class Parser(object):
    def __init__(self, namespace):
        self.namespace = namespace
        self.special = {'\'', '\"', '$', '=', '|', ' '}

    def parse(self, command):
        res = []
        buf = ''
        for symbol in command:
            if symbol not in self.special:
                buf += symbol
            else:
                res.append(buf)
                res.append(symbol)
                buf = ''

        res.append(buf)
        commands_and_arguments = []

        return res
