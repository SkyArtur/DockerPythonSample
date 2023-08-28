from dataclasses import dataclass


@dataclass
class Contact:
    telephone: str | None = None
    email: str | None = None

    def __repr__(self):
        return self.__str__()

    def __str__(self):
        return str(
            f'Telefone: {self.telephone}'
            f'\n{"Email: " + self.email if self.email is not None else ""}'
        ).strip()
