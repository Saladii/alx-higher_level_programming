#!/usr/bin/python3
''' A class Square that defines a square by:
    Private instance attribute: size
    Instantiation with Instantiation with optional size
    - size must be an integer
'''


class Square():
    '''calss constructor'''
    def __int__(self, size=0):
        if type(size) != int:
            raise TypeError:
                print('size must be an integer')
        if size < 0:
            raise ValueError:
                print('size must be >= 0')
        self._size = size
