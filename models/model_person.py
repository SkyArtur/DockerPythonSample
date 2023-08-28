import json
from pathlib import Path
from objects import Person


class ModelPerson(Person):
    __instance = None
    __path = Path(__file__).resolve().parent.parent.joinpath('db/students.json')

    def __new__(cls, *args, **kwargs):
        if cls.__instance is None or not cls.__instance:
            cls.__instance = super(ModelPerson, cls).__new__(cls)
        return cls.__instance

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.__check_files()

    def __check_files(self):
        if not self.__path.exists():
            self.__write_file({})

    def __read_file(self):
        with open(self.__path, 'r', encoding='utf8') as file:
            return json.load(file)

    def __write_file(self, data):
        with open(self.__path, 'w', encoding='utf-8') as file:
            json.dump(data, file, ensure_ascii=False, indent=2)

    def __gen_id(self):
        data_file, new_id = self.__read_file(), 1
        if len(data_file) != 0:
            for key in data_file.keys():
                new_id = int(key)
            new_id += 1
        self.id = new_id
        return new_id

    def fetchone(self):
        try:
            self.__dict__.update(self.__read_file()[f'{self.id}'])
        except KeyError:
            print('Pessoa não encontrada!')
            return False
        else:
            print(f'{"+" * 50}', self, f'{"+" * 50}', sep='\n')
            return True

    def fetchall(self):
        try:
            print(f"{'id':^7}|{'Nome':^20}|{'Sobrenome':^37}|{'Nascimento':^15}|{'CPF':^18}\n{'-' * 100}")
            for item in self.__read_file().values():
                self.__dict__.update(item)
                print(f"{self.id:^7}| {self.first_name:<19}|  {self.last_name:<35}|{self.birth:^15}|{self.cpf:^18}")
        except FileNotFoundError:
            print('Arquivo não encontrado!')
            return False
        else:
            return True

    def save(self):
        try:
            data_file = self.__read_file()
            data_file.update({f'{self.__gen_id()}': self.__dict__})
            self.__write_file(data_file)
        except json.JSONDecodeError:
            print('Não foi possível salvar no banco de dados')
            return False
        else:
            return True

    def update(self):
        try:
            data_file = self.__read_file()
            data_file[f'{self.id}']['first_name'] = self.first_name
            data_file[f'{self.id}']['last_name'] = self.last_name
        except KeyError:
            print('Pessoa não encontrada!')
            return False
        else:
            self.__write_file(data_file)
            return True

    def delete(self):
        try:
            data_file = self.__read_file()
            data_file.pop(f'{self.id}')
            self.__write_file(data_file)
        except KeyError:
            print('Pessoa não encontrada!')
            return False
        else:
            return True
