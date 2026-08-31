import unittest

from app.database.database import SessionLocal
class TestDatabase(unittest.TestCase):

    def test_database_connection(self):
        db_session = SessionLocal()

        self.assertIsNotNone(db_session)

        db_session.close()


if __name__ == "__main__":
    unittest.main()