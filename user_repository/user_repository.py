from expression import Error, Ok
import user_repository


class UnknownRepositoryError(Exception):
    def __init__(self, action) -> None:
        super().__init__()
        self.action = action


class UserRepository(object):
    def __init__(self, database) -> None:
        self.database = database

    def create(self, user):
        try:
            self.database['User'].create(username=user['username'])
            return Ok('user created successfully')
        except:
            return Error(UnknownRepositoryError('create new user'))


def create_user_repository(database):
    if user_repository._repository:
        return user_repository._repository
    user_repository._repository = UserRepository(database)
    return user_repository._repository
