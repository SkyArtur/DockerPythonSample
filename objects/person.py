from .data_objects import Personal, Document


class Person(Personal, Document):
    def __init__(self, **kwargs):
        self.id = kwargs.get('id')
        self.first_name = kwargs.get('first_name')
        self.last_name = kwargs.get('last_name')
        self.birth = kwargs.get('birth')
        self.cpf = kwargs.get('cpf')

    def __str__(self):
        return str(
            f'\n{Personal.__str__(self)}'
            f'\n{Document.__str__(self)}'
        )
