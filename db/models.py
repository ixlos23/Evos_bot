from ORM.ORMM import DB


class User(DB):
    def __init__(self,
                 *param,
                 user_id: int = None,
                 first_name: str = None,
                 last_name: str = None,
                 username: str = None,
                 phone_number: str = None,
                 lang: str = 'en',
                 ):
        self.param = param
        self.user_id = user_id
        self.first_name = first_name
        self.last_name = last_name
        self.username = username
        self.phone_number = phone_number
        self.lang = lang


class Region(DB):
    def __init__(self, *param, id: int = None, name: str = None):
        self.id = id
        self.name = name
        self.param = param