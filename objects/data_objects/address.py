class Address:
    def __init__(self, **kwargs):
        self.street: str = kwargs.get('street')
        self.number: str = kwargs.get('number')
        self.cep: str = kwargs.get('cep')
        self.neighborhood = kwargs.get('neighborhood')
        self.city = kwargs.get('city')
        self.state = kwargs.get('state')

    def __repr__(self):
        return self.__str__()

    def __str__(self):
        return str(
            f'Endereço: {self.street}, {self.number}'
            f'{"  -  CEP: " + self.cep if self.cep is not None else ""}'
            f'\n{self.neighborhood if self.neighborhood is not None else ""}'
            f'{"  -  " + self.city if self.city is not None else ""}'
            f'{"  -  " + self.state  if self.state is not None else ""}'
        ).strip()
