# DockerSamplePython
Pretende fornecer suporte didático e acompanhamento durante o treinamento em Python e Docker. O projeto em si deve ser
iniciado uma breve apresentação explicativa sobre a estrutura adotada. Esta estrutura é exemplificada em um simple
organograma de fluxo, demonstrando a relação entre os diferentes diretórios do sistema proposto conforme a imagem a 
seguir.
![docker_python_organograma.png](files%2Fimages%2Fdocker_python_organograma.png)

De forma simplificada temos relações entre objetos que começa pelas classes de dados e pelas models que manipulam
um arquivo json para persistência de dados. As views herdam as models e gerenciam as operações em arquivo de dados.
O controller por sua vez, instancia as view e disponibiliza o método de execução. O arquivo main.py, fica sendo 
responsável por executar as operações do controller.

### 1ª Parte - Functions

O módulo 'functions' terá, entre outros, o módulo 'inputs' que fornecerá os mecanismos para coleta e tratamento de 
dados da aplicação. Cinco funções foram desenvolvidas para este objetivo. Um conhecimento básico sobre funções é 
necessário, pois, para este projeto foi escolhido como foco para a implementação das funções, assuntos como 
recursividade e decoradores.

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
a responsabilidade de tratar os dados específicos que recebem e sinalizarem para o pattern o dado recebido validado e 
tratado ou None, caso a validação falhe.

### 2ª Parte - Objects

A segunda parte consiste da criação dos objetos de dados que serão usados para construir objetos mais complexos. Estes
objetos são dataclasses que fornecerão atributos para os objetos maiores. Os objetos maiores, então, escolhem quais 
atributos irá instanciar. Os objetos de dados também possuirão uma forma de exibir seus dados com mais inteligência 
utilizando operações ternárias dentro de f-strings.
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

###  3ª Parte - Models
Construção da model para manipulação do arquivo que será usado para persistência de dados. A model é um objeto singleton
que servirá de uma pequena introdução ao assunto "Design Patterns". Ele será responsável por ler e escrever em um arquivo
json e será uma extensão do objeto criado anteriormente. É interessante que atributos do objeto sejam utilizados, como 
o método __dict__ e etc. A model então implementa os métodos necessários para manipular o arquivo da dados.
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