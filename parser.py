import os
import sys

import model

# TODO: separate all the parsers and the helping functions (clear_screen and print_activity)


def clear_screen():
    _ = os.system('cls' if os.name == 'nt' else 'clear')


def print_activity(activity):
    id, task, created_at, updated_at = activity

    row = f"{id} - {task} - ({created_at} - {updated_at if updated_at else 'not updated'})"
    print(row)


class CoreParser:

    def __init__(self, option):
        self.print_message = option.print_message
        self.requires_input = option.requires_input

        self.command = option.command
        self.id = option.id
        self.task = option.task

        if self.requires_input:
            self.input_activity = option.input_activity

    def _parse_create_activity(self):
        if model.create_activity():
            print("create activity successful")
        else:
            print("create activity unsuccessful")

    def _parse_read_an_activity(self):
        activity = model.read_an_activity(self.id)

        if activity:
            print_activity(activity)
        else:
            print(f"There is no activity with id: {self.id}")

    def _parse_read_all_activities(self):
        activities = model.read_all_activities()

        if activities:
            for activity in activities:
                print_activity(activity)
        else:
            print(f"There is no activity")

    def _parse_update_an_activity(self):
        if model.update_an_activity(self.id, self.task):
            print("update activity successful")
        else:
            print("update activity unsuccessful")

    def _parse_delete_an_activity(self):
        if model.delete_an_activity(self.id):
            print("delete activity successful")
        else:
            print("delete activity unsuccessful")

    def _parse_delete_all_activities(self):
        if model.delete_all_activities():
            print("delete all activities successful")
        else:
            print("delete all activity unsuccessful")

    def run_core_parser(self):

        if self.command == "1":
            self._parse_create_activity()
        elif self.command == "2":
            self._parse_read_an_activity()
        elif self.command == "3":
            self._parse_read_all_activities()
        elif self.command == "4":
            self._parse_update_an_activity()
        elif self.command == "5":
            self._parse_delete_an_activity()
        elif self.command == "6":
            self._parse_delete_all_activities()
        elif self.command == "7":
            clear_screen()
            sys.exit()
        elif self.command == "clear" and self.requires_input:
            clear_screen()
            self.print_message()
            self.input_activity()
        else:
            clear_screen()
            sys.exit()


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

            if self.command == '4':
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
            '''
        print(message)


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
    '''

    def __init__(self, parsed_input):
        self.requires_input = False
        self.command = ""
        self.id = 0
        self.task = ""

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
        '''
        print(tutorial)

    def input_activity(self, input_data):
        if len(input) > 2:
            self.command = input_data[1]

            if self.command in ['read', 'update', 'delete']:
                self.id = input_data[2]

            if self.command in ['add', 'update']:
                self.task = input_data[3]
