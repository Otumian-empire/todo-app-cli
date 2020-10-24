import unittest

from model import DB


class TestModelsDB(unittest.TestCase):

    db = DB()

    def test_1_get_db_conn(self):
        self.assertIsNotNone(self.db.get_db_conn())

    def test_2_get_cursor(self):
        conn = self.db.get_db_conn()
        self.assertIsNotNone(self.db.get_db_conn())


if __name__ == '__main__':
    unittest.main()
