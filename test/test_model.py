import unittest

from model import Todo
from util import do_check_table


class TestModelsTodo(unittest.TestCase):

    drop_table_if_exists_todo = do_check_table

    drop_table_if_exists_todo(
        "DROP TABLE IF EXISTS todos",
        "There was an error in dropping table",
        "Table dropped successfully")

    sql_query = "CREATE TABLE IF NOT EXISTS `todos`(`id` int(11) PRIMARY KEY NOT NULL AUTO_INCREMENT, `task` varchar(255) NOT NULL, `created_at` timestamp NOT NULL DEFAULT current_timestamp(), `update_at` timestamp NULL DEFAULT NULL)"

    create_table_if_not_exists_todo = do_check_table

    create_table_if_not_exists_todo(
        sql_query,
        "There was an error while creating table",
        "Table created successfully")

    def test_1_create_activity_1(self):
        todo = Todo()
        result1 = todo.create_activity("Drink milk at 12pm")
        self.assertTrue(result1)

    def test_2_create_activity_2(self):
        todo = Todo()
        result2 = todo.create_activity("Go to the gym at 5:30pm")
        self.assertTrue(result2)

    def test_3_read_all_activities(self):
        todo = Todo()
        result = todo.read_all_activities()
        self.assertTrue(len(result) > 0)

    def test_4_read_an_activity(self):
        todo = Todo()
        result = todo.read_an_activity(1)
        self.assertTrue(len(result) > 0)

    def test_5_update_an_activity(self):
        todo = Todo()
        result = todo.update_an_activity(1, "Drink milk with cocoa tea at 1pm")
        self.assertTrue(result)

    def test_6_delete_an_activity(self):
        todo = Todo()
        result = todo.delete_an_activity(2)
        self.assertTrue(result)

    def test_7_delete_all_activities(self):
        todo = Todo()
        result = todo.delete_all_activities()
        self.assertTrue(result)


if __name__ == '__main__':
    unittest.main()
