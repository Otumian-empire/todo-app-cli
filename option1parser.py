class Option1Parser:
    '''
    1 - add an activity
    2 - read an activity
    3 - read all activities
    4 - update an activity
    5 - delete an activity
    6 - delete all activities
    7 - exit
    clear - clear the screen
    doc - display simple tutorial
    '''

    def __init__(self):
        self.requires_input = True
        self.print_message()
        self.input_activity()

    def input_activity(self):
        self.command = input(">>> Enter command option: ")
        self.id = 0
        self.task = ""

        if self.command in ['2', '4', '5']:
            self.id = input(">>> Enter task id: ")

        if self.command in ['1', '4']:
            self.task = input(">>> Enter task: ")

    def print_message(self):
        message = '''
            1 - add an activity
            2 - read an activity
            3 - read all activities
            4 - update an activity
            5 - delete an activity
            6 - delete all activities
            7 - exit
            clear - clear the screen
            doc - display simple tutorial
            '''
        print(message)

