class parser(object):
    def __init__(self):
        self.operators = {'=', 'wc', 'cat', 'echo', 'pwd'}

    def parse(self, command):
        res = [command]
        for operator in self.operators:
            new_res = []
            for command in res:
                splitted = command.split(operator)
                print(splitted)
                if len(splitted) > 1:
                    for tag in splitted:
                        new_res.extend([operator, tag])
            res = new_res
        return res
