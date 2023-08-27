from .data_objects import *


class Person(Personal, Contact, Address):
    def __init__(self, **kwargs):
        Personal.__init__(self, **kwargs)
        Contact.__init__(self, **kwargs)
        Address.__init__(self, **kwargs)

    def __str__(self):
        return str(
            f'{Personal.__str__(self)}\n'
            f'{Contact.__str__(self)}\n'
            f'{Address.__str__(self)}'
        ).strip()
