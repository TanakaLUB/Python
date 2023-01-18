
import unittest


class DBTest(unittest.TestCase):
    def test_db(self):
        from infra.dbUtil import DB

        db = DB()
        result = db.select("aaaa")
        self.assertEqual(result.user_id, "aaaa")

    def test_create(self):
        pass


if __name__ == "__main__":
    db = DBTest()
    db.test_db()
