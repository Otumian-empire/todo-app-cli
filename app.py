import sys
from parser import CoreParser, Option1Parser, Option2Parser

if __name__ == "__main__":

    if len(sys.argv) > 1:
        # TODO
        # pass sys.argv[1:] to the Option2Parser to get command, id and task
        option = Option2Parser()
    else:
        option = Option1Parser()

    app = CoreParser(option)
    app.run_core_parser()
