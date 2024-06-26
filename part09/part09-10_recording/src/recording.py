# WRITE YOUR SOLUTION HERE:
class Recording:
    def __init__(self, duration):
        if duration >= 0:
            self.__length = duration
        else:
            raise ValueError('Please type in a valid length')
    
    @property
    def length(self):
        return self.__length
    
    @length.setter
    def length(self, duration):
        if duration >= 0:
            self.__length = duration
        else:
            raise ValueError('Please type in a valid length')