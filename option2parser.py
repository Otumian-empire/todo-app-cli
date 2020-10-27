class Option2Parser:
    '''
    - add activity
    - read activity_id
    - read *
    - read all
    - update activity_id new_task
    - delete activity_id
    - delete *
    - delete all
    - clear - clear the screen
    - doc - display simple tutorial
    '''

    def __init__(self, parsed_input):
        self.requires_input = False
        self.command = ""
        self.id = 0
        self.task = ""

        self.input_activity(parsed_input)

    def print_message(self):
        tutorial = '''
        This is a simple tutorial on how to run app on terminal

        add "Call John Doe at 2pm"
        (This is adds a new activity)

        read 2
        (This reads an activity with id=2)

        read all
        read *
        (This reads all the activities - the id is all or *)

        update 2 "Call John Doe at 3pm"
        (This update an activity with id=2 with the text as task)

        delete 2
        (This deletes an activity with id=2)

        delete all
        delete *
        (This deletes all there activities - the id is all or *)

        clear - clears the screen

        doc - display simple tutorial
        '''
        print(tutorial)

    def input_activity(self, input_data):
        
        self.command = input_data[0]

        if self.command == 'add':
            self.task = input_data[1]

        if self.command in ['read', 'update', 'delete']:
            self.id = input_data[1]

        if self.command == 'update':
            self.task = input_data[2]
