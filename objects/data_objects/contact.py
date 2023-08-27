class Contact:
    def __init__(self, **kwargs):
        self.telephone = kwargs.get('telephone')
        self.email = kwargs.get('email')

    def __repr__(self):
        return self.__str__()

    def __str__(self):
        return str(
            f'Telefone: {self.telephone}'
            f'\n{"Email: " + self.email if self.email is not None else ""}'
        ).strip()
