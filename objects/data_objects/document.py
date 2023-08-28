from dataclasses import dataclass


@dataclass
class Document:
    cpf: str | None = None
    rg: str | None = None
    cnh: str | None = None

    def __repr__(self):
        return self.__str__()

    def __str__(self):
        return str(
            f'CPF: {self.cpf}'
            f'\n{"RG: " + self.rg if self.rg is not None else ""}'
            f'\n{"CNH: " + self.cnh if self.cnh is not None else ""}'
        ).strip()
