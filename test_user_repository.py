import unittest
from user_repository.user_repository import create_user_repository
from database.database import create_database


mock_student_1 = {'username': 'mario'}


class TestUserRepository(unittest.TestCase):
    def setUp(self) -> None:
        super().setUp()
        self.models = create_database()
        self.user_repository = create_user_repository(self.models)

    def tearDown(self) -> None:
        super().tearDown()
        self.models['User'].delete()

    def test_creatingANewUser_shouldBeOk(self):
        result = self.user_repository.create(mock_student_1)
        self.assertTrue(result.is_ok())

    def test_creatingDuplicatedUsers_shouldBeAnError(self):
        self.user_repository.create(mock_student_1)
        result = self.user_repository.create(mock_student_1)
        self.assertTrue(result.is_error())

    def test_deletingAUser_shouldBeOk(self):
        self.user_repository.create(mock_student_1)
        result = self.user_repository.delete('mario')
        self.assertTrue(result.is_ok())

    def test_deletingAnUnknownUser_shouldBeOk(self):
        self.user_repository.create(mock_student_1)
        result = self.user_repository.delete('victor')
        self.assertTrue(result.is_ok())
