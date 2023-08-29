from models import ModelPerson
from functions import *


class ViewPerson:
    __person = ModelPerson()

    @classmethod
    def new_person(cls):
        print(f"\n{'-' * 100}\n{'Cadastrar nova Pessoa':^100}\n{'-' * 100}\n")
        cls.__person.first_name = input_name('Digite o primeiro nome: ')
        cls.__person.last_name = input_name('Digite o sobrenome: ')
        cls.__person.birth = input_date('Digite a data de nascimento: ')
        cls.__person.cpf = input_cpf('Digite o CPF: ')
        print(cls.__person)
        cls.__person.save()

    @classmethod
    def update_person(cls):
        print(f"\n{'-' * 100}\n{'Atualizar nome de uma Pessoa':^100}\n{'-' * 100}\n")
        cls.__person.fetchall()
        cls.__person.id = input_numeric('Digite o id da Pessoa: ')
        cls.__person.first_name = input_name('Digite o novo nome: ')
        cls.__person.last_name = input_name('Digite o novo sobrenome: ')
        cls.__person.update()
        cls.__person.fetchall()

    @classmethod
    def delete_person(cls):
        print(f"\n{'-' * 100}\n{'Deletar uma Pessoa':^100}\n{'-' * 100}\n")
        cls.__person.fetchall()
        cls.__person.id = input_numeric('Digite o id da Pessoa: ')
        cls.__person.delete()
        cls.__person.fetchall()

    @classmethod
    def get_one_person(cls):
        print(f"\n{'-' * 100}\n{'Procurar Pessoa por id':^100}\n{'-' * 100}\n")
        cls.__person.id = input_numeric('Digite o id que deseja procurar: ')
        cls.__person.fetchone()

    @classmethod
    def get_all_persons(cls):
        print(f"\n{'-' * 100}\n{'Visualizar todas as Pessoas':^100}\n{'-' * 100}\n")
        cls.__person.fetchall()
