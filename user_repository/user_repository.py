import sys
import user_repository
from expression import Error, Ok


class UnknownRepositoryError(Exception):
    def __init__(self, action) -> None:
        super().__init__()
        self.action = action


class UserRepository(object):
    def __init__(self, models) -> None:
        self.User = models['User']

    def create(self, user):
        try:
            self.User.create(username=user['username'])
            return Ok('user created successfully')
        except:
            return Error(UnknownRepositoryError('create new user'))

    def delete(self, id):
        try:
            self.User.delete().where(self.User.username == id).execute()
            return Ok('user deleted successfully')
        except:
            return Error(UnknownRepositoryError('delete user'))


def create_user_repository(database):
    if user_repository._repository:
        return user_repository._repository
    user_repository._repository = UserRepository(database)
    return user_repository._repository
