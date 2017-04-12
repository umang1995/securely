class UserBasicInfoVo(object):
    def __init__(self):
        self._username = None
        self._name = None
        self._email = None
        self._file_uploaded = None

    @property
    def username(self):
        self._username

    @username.setter
    def username(self, value):
        self._username = value

    @property
    def name(self):
        self._name

    @name.setter
    def name(self, value):
        self._name = value

    @property
    def email(self):
        self._email

    @email.setter
    def email(self, value):
        self._email = value

    @property
    def file_uploaded(self):
        self._file_uploaded

    @file_uploaded.setter
    def file_uploaded(self, value):
        self._file_uploaded = value

    def serialize(self):
        return {
            'username': self._username,
            'name': self._name,
            'email': self._email,
            'file_uploaded': self._file_uploaded
        }
