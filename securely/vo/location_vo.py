class LocationVo(object):
    def __init__(self):
        self._latitude = None
        self._longitude = None

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

    def serialize(self):
        return {
            'latitude': self._latitude,
            'longitude': self._longitude
        }


