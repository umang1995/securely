class FileVo(object):
    def __init__(self):
        self._id = None
        self._location = None
        self._ss = None
        self._password = None
        self._longitude = None
        self._latitude = None
        self._username = None
        self._IV = None
        self._key = None

    @property
    def key(self):
        self._key

    @key.setter
    def key(self, value):
        self._key = value

    @property
    def id(self):
        self._id

    @id.setter
    def id(self, value):
        self._id = value

    @property
    def location(self):
        self._location

    @location.setter
    def location(self, value):
        self._location = value

    @property
    def ss(self):
        self._ss

    @ss.setter
    def ss(self, value):
        self._ss = value

    @property
    def password(self):
        self._password

    @password.setter
    def password(self, value):
        self._password = value

    @property
    def latitude(self):
        self._latitude

    @latitude.setter
    def latitude(self, value):
        self._latitude = value

    @property
    def longitude(self):
        self._longitude

    @longitude.setter
    def longitude(self, value):
        self._longitude = value

    @property
    def username(self):
        self._username

    @username.setter
    def username(self, value):
        self._username = value

    @property
    def IV(self):
        self._IV

    @IV.setter
    def IV(self, value):
        self._IV = value

