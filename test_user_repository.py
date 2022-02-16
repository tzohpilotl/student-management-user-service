import unittest
from user_repository.user_repository import create_user_repository
from database.database import create_database


class TestUserRepository(unittest.TestCase):
    def setUp(self) -> None:
        super().setUp()
        database = create_database()
        self.user_repository = create_user_repository(database)

    def test_creatingANewUser_shouldBeOk(self):
        result = self.user_repository.create({'username': 'mario'})
        self.assertTrue(result.is_ok())
