import unittest
from user_service import UserService
from database.database import create_database

mock_admin = {'role': 'mock_admin', 'username': 'mario'}
mock_root = {'role': 'root', 'username': 'mario'}
mock_student = {'username': 'victor'}


class TestUserServiceRoles(unittest.TestCase):
    def setUpClass(self) -> None:
        self.mock_repositories = create_database()

    def test_when_credentialsHaveAdminRole_theUserServiceOnlyHandlesStudents(self):
        user_service = UserService.create_user(
            mock_admin, self.mock_repositories)
        self.assertTrue(user_service.register_student({}).is_ok())
        self.assertTrue(user_service.deregister_student('adminId').is_ok())
        self.assertTrue(user_service.update_student({}, 'adminId').is_ok())
        self.assertTrue(user_service.register_admin({}).is_error())
        self.assertTrue(
            user_service.deregister_admin('adminId').is_error())
        self.assertTrue(user_service.update_admin(
            {}, 'adminId').is_error())

    def test_when_credentialsHaveRootRole_theUserServiceCanManageAdminsAndStudents(self):
        user_service = UserService.create_user(
            mock_root, self.mock_repositories)
        self.assertTrue(user_service.register_student({}).is_ok())
        self.assertTrue(user_service.deregister_student('adminId').is_ok())
        self.assertTrue(user_service.update_student({}, 'adminId').is_ok())
        self.assertTrue(user_service.register_admin({}).is_ok())
        self.assertTrue(user_service.deregister_admin('adminId').is_ok())
        self.assertTrue(user_service.update_admin({}, 'adminId').is_ok())


class TestAdminUserService(unittest.TestCase):
    def setUp(self) -> None:
        mock_repositories = create_database()
        self.user_service = UserService.create_user(
            mock_admin, mock_repositories)

    def test_when_anAdminCreatesAStudent_theRequestIsHandledCorrectly(self):
        result = self.user_service.register_student(mock_student)
        self.assertTrue(result.is_ok())
