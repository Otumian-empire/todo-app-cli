import sys
from parser import CoreParser

from option1parser import Option1Parser
from option2parser import Option2Parser

if __name__ == "__main__":

    if len(sys.argv) > 1:
        option = Option2Parser(sys.argv[1:])
    else:
        option = Option1Parser()

    app = CoreParser(option)
    app.run_core_parser()
