from src import functions, parser, checker
import os


if __name__ == '__main__':
    global_namespace = dict()
    prsr = parser.Parser(global_namespace)

    chckr = checker.checker()
    new_command = input(str(os.getcwd()) + '>> ')
    print(prsr.parse(new_command))
    while True:
        try:
            command = prsr.parse(new_command)
            if command[0] == 'ls':
                if len(command) > 3:
                    print("ls takes zero or one parameter")
                else:
                    if len(command) == 1 or len(command) == 2:
                        res = os.listdir(os.getcwd())
                        for folder in res:
                            print(folder)
                    else:
                        res = os.listdir(command[2])
                        for folder in res:
                            print(folder)
            if command[0] == 'cd':
                if len(command) > 3:
                    print("ls takes zero or one parameter")
                else:
                    if len(command) == 1 or len(command) == 2:
                        os.chdir(os.getcwd())
                    else:
                        os.chdir(command[2])
            global_namespace = dict()
            prsr = parser.Parser(global_namespace)
            chckr = checker.checker()
            new_command = input(str(os.getcwd()) + '>> ')
        except KeyboardInterrupt:
            exit(0)
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
