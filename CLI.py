from src import functions, parser, checker


if __name__ == '__main__':
    prsr = parser.parser()
    chckr = checker.checker()
    new_command = ''
    while True:
        new_command += input('>> ')
        if new_command == 'exit':
            break
        cmd_arr = prsr.parse(new_command)
        print(cmd_arr)
        if chckr.check(cmd_arr):
            functions.apply(cmd_arr)
        new_command = ''
