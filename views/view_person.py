from models import ModelPerson
from functions import *


class ViewPerson:
    person = ModelPerson()

    @classmethod
    def new_person(cls):
        print(f"\n{'-' * 100}\n{'Cadastrar nova Pessoa':^100}\n{'-' * 100}\n")
        cls.person.first_name = input_name('Digite o primeiro nome: ')
        cls.person.last_name = input_name('Digite o sobrenome: ')
        cls.person.birth = input_date('Digite a data de nascimento: ')
        cls.person.cpf = input_cpf('Digite o CPF: ')
        cls.person.save()

    @classmethod
    def update_person(cls):
        print(f"\n{'-' * 100}\n{'Atualizar nome de uma Pessoa':^100}\n{'-' * 100}\n")
        cls.person.id = input_numeric('Digite o id da Pessoa: ')
        cls.person.first_name = input_name('Digite o novo nome: ')
        cls.person.last_name = input_name('Digite o novo sobrenome: ')
        cls.person.update()

    @classmethod
    def delete_person(cls):
        print(f"\n{'-' * 100}\n{'Deletar uma Pessoa':^100}\n{'-' * 100}\n")
        cls.person.id = input_numeric('Digite o id da Pessoa: ')
        cls.person.delete()

    @classmethod
    def get_one_person(cls):
        print(f"\n{'-' * 100}\n{'Procurar Pessoa por id':^100}\n{'-' * 100}\n")
        cls.person.id = input_numeric('Digite o id que deseja procurar: ')
        cls.person.fetchone()

    @classmethod
    def get_all_persons(cls):
        print(f"\n{'-' * 100}\n{'Visualizar todas as Pessoas':^100}\n{'-' * 100}\n")
        cls.person.fetchall()
