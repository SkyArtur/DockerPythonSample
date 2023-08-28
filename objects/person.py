from .data_objects import Personal, Document


class Person(Personal, Document):
    def __init__(self, **kwargs):
        self.__id = kwargs.get('id')
        self.first_name = kwargs.get('first_name')
        self.last_name = kwargs.get('last_name')
        self.birth = kwargs.get('birth')
        self.cpf = kwargs.get('cpf')

    @property
    def id(self):
        return int(self.__id)

    @id.setter
    def id(self, value: int):
        self.__id = value

    def __str__(self):
        return str(
            f'{Personal.__str__(self)}'
            f'\n{Document.__str__(self)}'
        )
