from dataclasses import dataclass
from datetime import date


@dataclass
class Personal:
    first_name: str | None = None
    last_name: str | None = None
    birth: str | None = None

    @property
    def age(self):
        age = [int(i) for i in self.birth.split('/')]
        age = date(day=age[0], month=age[1], year=age[2])
        return (date.today() - age).days // 365 if self.birth is not None else None

    def __repr__(self):
        return self.__str__()

    def __str__(self):
        return str(
            f'Nome: {self.first_name} {self.last_name if self.last_name is not None else ""}'
            f'\n{"Data Nascimento: " + self.birth if self.birth is not None else ""}'
            f'{"  -  " + str(self.age) + " anos" if self.birth is not None else ""}'
        ).strip()
