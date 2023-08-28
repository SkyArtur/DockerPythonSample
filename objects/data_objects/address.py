from dataclasses import dataclass


@dataclass
class Address:
    street: str | None = None
    number: str | None = None
    cep: str | None = None
    neighborhood: str | None = None
    city: str | None = None
    state: str | None = None

    def __repr__(self):
        return self.__str__()

    def __str__(self):
        return str(
            f'Endereço: {self.street}, {self.number}'
            f'{"  -  CEP: " + self.cep if self.cep is not None else ""}'
            f'\n{self.neighborhood if self.neighborhood is not None else ""}'
            f'{"  -  " + self.city if self.city is not None else ""}'
            f'{"  -  " + self.state if self.state is not None else ""}'
        ).strip()
