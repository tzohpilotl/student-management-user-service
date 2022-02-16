from enum import unique
import peewee

database = peewee.SqliteDatabase(None)


class User(peewee.Model):
    username = peewee.CharField(unique=True)

    class Meta:
        database = database


def setup_database():
    try:
        User.create_table()
    except peewee.OperationalError:
        print("User table exists.")


def create_database(environment='test', database_name='huracanes'):
    match environment:
        case 'test':
            database.init(':memory:')
        case 'production':
            database.init(F"{database_name}_production")
        case 'development':
            database.init(F"{database_name}_development")

    setup_database()
    return {'database': database, 'User': User}
