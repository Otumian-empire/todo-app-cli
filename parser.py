import sys

from model import Todo
from util import clear_screen, print_activity


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
        if Todo().create_activity(self.task):
            print("create activity successful")
        else:
            print("create activity unsuccessful")

    def _parse_read_an_activity(self):
        activity = Todo().read_an_activity(self.id)

        if activity:
            print_activity(activity)
        else:
            print(f"There is no activity with id: {self.id}")

    def _parse_read_all_activities(self):
        activities = Todo().read_all_activities()

        if activities:
            for activity in activities:
                print_activity(activity)
        else:
            print(f"There is no activity")

    def _parse_update_an_activity(self):
        if Todo().update_an_activity(self.id, self.task):
            print("update activity successful")
        else:
            print("update activity unsuccessful")

    def _parse_delete_an_activity(self):
        if Todo().delete_an_activity(self.id):
            print("delete activity successful")
        else:
            print("delete activity unsuccessful")

    def _parse_delete_all_activities(self):
        if Todo().delete_all_activities():
            print("delete all activities successful")
        else:
            print("delete all activity unsuccessful")

    def run_core_parser(self):

        if self.command == "1" or self.command == "add":
            self._parse_create_activity()

        elif self.command == "2" or (
                self.command == "read" and self.id not in ["all", "*"]):
            self._parse_read_an_activity()

        elif self.command == "3" or (
                self.command == "read" and self.id in ["all", "*"]):
            self._parse_read_all_activities()

        elif self.command == "4" or self.command == "update":
            self._parse_update_an_activity()

        elif self.command == "5" or (
                self.command == "delete" and self.id not in ["all", "*"]):
            self._parse_delete_an_activity()

        elif self.command == "6" or (
                self.command == "delete" and self.id in ["all", "*"]):
            self._parse_delete_all_activities()

        elif self.command == "7" or self.command in ["exit", "quit"]:
            clear_screen()
            sys.exit()

        elif self.command == "clear":
            clear_screen()

            if self.requires_input:
                self.print_message()
                self.input_activity()

        elif self.command in [
                "doc", "tut", "documentation", "tutorial", "guide"]:
            clear_screen()
            self.print_message()

        else:
            clear_screen()
            sys.exit()
