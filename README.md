# DockerSamplePython

### Sobre o projeto
Pretende fornecer suporte didático e acompanhamento durante o treinamento em Python e Docker. O projeto em si deve ser
iniciado com uma breve apresentação explicativa sobre a estrutura adotada. Esta estrutura é exemplificada em um simples
organograma de fluxo, demonstrando a relação entre os diferentes diretórios do sistema proposto conforme a imagem a 
seguir.

![docker_python_organograma.png](files%2Fimages%2Fdocker_python_organograma.png)

De forma simplificada temos relações entre objetos que começam pelas classes básicas para dados. A model que manipula
um arquivo json para persistência de dados, herda atributos destas classes básicas. A view instancia a model por 
atribuição e passa a gerenciar a coleta de dados e as operações em arquivo de dados. O controller por sua vez, instancia
a view e disponibiliza o método de execução. O arquivo main.py, fica sendo responsável por executar as operações do
controller.

### 1ª Parte - Functions

O módulo 'functions' terá internamente, o módulo 'inputs' que fornecerá os mecanismos para coleta e tratamento de 
dados da aplicação. Cinco funções foram desenvolvidas para este objetivo. Um conhecimento básico sobre funções é 
necessário. Os assuntos trabalhados nesta parte são:
- Funções;
- *args & **kwargs;
- Funções decoradoras;
- Recursividade de funções;
```python
def input_pattern(input_any):
    def _input(label_input: str, __control: int = 5, **kwargs) -> str | float:
        user_input = input_any(input(label_input), **kwargs)
        if user_input is None:
            if __control > 0:
                return _input(label_input, __control - 1, **kwargs)
            else:
                raise RuntimeError('Limite da chamadas recursivas.')
        return user_input

    return _input


@input_pattern
def input_anything(user_input: str):
    _input_user = user_input
    if not _input_user:
        return None
    return _input_user
```
A função input_pattern(), é uma função decoradora que fornece o input para a função decorada enquanto espera que ela 
realize a validação e tratamento do dado fornecido, além disso, realiza a recursividade para dados incorretos e controla
o número de chamadas recursivas realizadas. Ficando assim para as demais funções (input_name(), input_date(), etc)
a responsabilidade de tratar os dados específicos que recebem e retornam para o pattern, o dado recebido, validado e 
tratado, ou None, caso a validação falhe.

### 2ª Parte - Objects

A segunda parte consiste da criação dos objetos de dados que serão usados para construir objetos mais complexos. Estes
objetos são dataclasses que fornecerão atributos para os objetos maiores. Os objetos maiores, então, escolhem quais 
atributos irá instanciar. Os objetos de dados também possuirão uma forma de exibir seus dados com mais inteligência 
realizando operações ternárias dentro de f-strings. Alguns dos assuntos trabalhados nesta parte são:
- Herança e polimorfismo;
- Príncipio de aberto e fechado;
- Dataclasses Python;
```python
from dataclasses import dataclass


@dataclass
class Personal:
    first_name: str | None = None
    last_name: str | None = None
    birth: str | None = None
    
    def __repr__(self):
        return self.__str__()
    
    def __str__(self):
        return str(
            f'Nome: {self.first_name} {self.last_name if self.last_name is not None else ""}'
            f'\n{"Nascimento: " + self.birth if self.birth is not None else ""}'
        ).strip()
    

@dataclass
class Document:
    cpf: str | None = None    
    rg: str | None = None
    
    def __repr__(self):
        return self.__str__()
    
    def __str__(self):
        return str(
            f'CPF: {self.cpf}'
            f'\n{"RG: " + self.rg if self.rg is not None else ""}'
        ).strip()
  
``` 
O objeto criado pode então escolher quais atributos instânciar, tendo em vista que estes objetos serão utilizados para
armazenar os dados em transações dentro do nosso sistema.
```python
from objects.data_objects import *


class Person(Personal, Document):
    def __init__(self, **kwargs):
        self.first_name = kwargs.get('first_name')
        self.last_name = kwargs.get('last_name')
        self.cpf = kwargs.get('cpf')

    def __str__(self):
        return str(
            f'\n{Personal.__str__(self)}'
            f'\n{Document.__str__(self)}'
        ).strip()

```

###  3ª Parte - Model

A model para manipulação do arquivo que será usado para persistência de dados, herdará o objeto de dados final. 
Ela é um objeto singleton, o quê servirá como uma pequena introdução ao assunto "Design Patterns". 
Como mencionado ela será responsável por ler e escrever em um arquivo json, e usará os atributos herdados pelo objeto de
dados, para manipular, gerir e circular estes dados entre a entrada e armazenamento. Os assuntos trabalhados aqui, são:
- Leitura e escrita em arquivos json.
- Estrutura de dados e coleções.
- Design Pattern Singleton;
- Atributos de classe e de instância;
- Atributos e métodos privados e públicos em Python;
```python
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
        ...

    ...
```

###  4ª Parte - View

A view é o elemento que faz a coleta dos dados. Ela faz isso instanciando a model como um atributo de classe privado e
disponibilizando uma série de 'class methods' que serão chamados pelo controller, como opções de um menu. Dentre os 
assuntos trabalhados, temos:
- Revisões;
- Métodos de classe;
```python
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
    ...
```
É interessante a observação sobre como a complexidade do sistema diminui a medida que dividimos as atribuições entre 
diferentes objetos do sistema. Desta forma, devido a sua natureza, alguns objetos terão atribuições e operações mais 
complexas, porém, objetos mais superficiais, que derivem destes objetos, podem usufruir de sua complexidade, para 
realizar operações mais simples.

### 5ª Parte - Controller e main.py 

Para esta parte 