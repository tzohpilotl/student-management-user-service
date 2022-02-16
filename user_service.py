from expression import Ok, Error
from user_repository.user_repository import create_user_repository


class AuthorizationError(Exception):
    def __init__(self, action, credentials):
        super().__init__()
        self.message = F"User {credentials['username']} is not authorized to {action}."


class Admin(object):
    def __init__(self, credentials={}, repositories={}):
        self.credentials = credentials
        self.User = repositories['User']

    def register_student(self, student):
        return self.User.create(student)

    def deregister_student(self, id):
        return self.User.delete(id)

    def update_student(self, update, studentId):
        return Ok('pass')

    def register_admin(self, admin):
        return Error(AuthorizationError("register administrators", self.credentials))

    def deregister_admin(self, adminId):
        return Error(AuthorizationError("deregister administrators", self.credentials))

    def update_admin(self, update, adminId):
        return Error(AuthorizationError("update administrators", self.credentials))


class Root(Admin):
    def register_admin(self, admin):
        return self.User.create(admin)

    def deregister_admin(self, id):
        return self.User.delete(id)

    def update_admin(self, update, adminId):
        return Ok('pass')


class UserService(object):
    @staticmethod
    def create_user(credentials, database):
        user_repository = create_user_repository(database)
        if credentials['role'] == 'root':
            return Root(credentials, {'User': user_repository})
        return Admin(credentials, {'User': user_repository})
