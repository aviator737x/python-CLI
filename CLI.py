from src import functions, parser, checker


if __name__ == '__main__':
    global_namespace = dict()
    prsr = parser.Parser(global_namespace)

    chckr = checker.checker()
    new_command = input('>> ')
    print(prsr.parse(new_command))
    # while True:
    #     new_command += input('>> ')
    #     if new_command == 'exit':
    #         break
    #     cmd_arr = prsr.parse(new_command)
    #     print(cmd_arr)
    #     if chckr.check(cmd_arr):
    #         functions.apply(cmd_arr)
    #     new_command = ''
    print()
