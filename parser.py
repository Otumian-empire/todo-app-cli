import os
import model


def clear_screen():
    _ = os.system('cls' if os.name == 'nt' else 'clear')


def print_activity(activity):
    id, task, created_at, updated_at = activity

    row = f"{id} - {task} - ({created_at} - {updated_at if updated_at else 'not updated'})"
    print(row)


class CoreParser:

    def __init__(self, option):
        self.command = option.command
        self.id = option.id
        self.task = option.task

        print(f"command: {self.command}")
        print(f"id: {self.id}")
        print(f"task: {self.task}")

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
        while self.command not in ['7', 'exit', 'quit']:
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
            else:
                clear_screen()
                exit()


class Option1Parser:
    '''
    1 - add an activity
    2 - read an activity
    3 - read all activities
    4 - update an activity
    5 - delete an activity
    6 - delete all activities
    7 - exit
    '''

    def __init__(self):
        print('''
            1 - add an activity
            2 - read an activity
            3 - read all activities
            4 - update an activity
            5 - delete an activity
            6 - delete all activities
            7 - exit
            ''')

        self.command = input(">>> Enter command option: ")
        self.id = 0
        self.task = ""

        if self.command in ['2', '4', '5']:
            self.id = input(">>> Enter task id: ")

            if self.command == '4':
                self.task = input(">>> Enter task: ")


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
    '''
    pass
