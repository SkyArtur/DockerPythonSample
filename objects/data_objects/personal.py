from datetime import date


class Personal:
    def __init__(self, **kwargs):
        self.first_name: str = kwargs.get('first_name')
        self.last_name: str = kwargs.get('last_name')
        self.birth: date = kwargs.get('birth')

    @property
    def age(self):
        return (date.today() - self.birth).days // 365 if self.birth is not None else None

    def __repr__(self):
        return self.__str__()

    def __str__(self):
        return str(
            f'\ue7fd DADOS PESSOAIS'
            f'\nNome: {self.first_name} {self.last_name if self.last_name is not None else ""}'
            f'\n{"Data Nascimento: " + self.birth.strftime("%d/%m/%Y") if self.birth is not None else ""}'
            f'{"  -  " + str(self.age) + " anos" if self.birth is not None else ""}'
        ).strip()



