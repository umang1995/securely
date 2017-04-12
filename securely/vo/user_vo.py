class UserVo(object):
    def __init__(self):
        self._file_uploaded = None
        self._location_uploaded = None

    @property
    def file_uploaded(self):
        self._file_uploaded

    @file_uploaded.setter
    def file_uploaded(self, value):
        self._file_uploaded = value


    @property
    def location_uploaded(self):
        self._location_uploaded

    @location_uploaded.setter
    def location_uploaded(self, value):
        self._location_uploaded = value


    def serialize(self):
        return {
            'file_uploaded':self._file_uploaded,
            'location_uploaded': self._location_uploaded.serialize()
        }
