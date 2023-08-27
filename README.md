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

### 1ª PARTE - Functions

O módulo 'functions' terá, entre outros, o módulo 'inputs' que fornecerá os mecanismos para coleta e tratamento de 
dados da aplicação. Cinco funções foram desenvolvidas para este objetivo. Um conhecimento básico sobre funções é 
necessário, pois, para este projeto foi escolhido como foco para a implementação das funções, assuntos como 
recursividade e decoradores.

```python
def decoradora(funcao):
    def interna(label, __control: int = 5, **kwargs):
        resposta = funcao(input(label), **kwargs)
        if resposta is None:
            print('Mensagem de erro!')
            return interna(label, __control - 1, **kwargs)
        return resposta
    return interna

@decoradora
def decorada(label, **kwargs):
    _input_user = label
    if not _input_user:
        return None
    return _input_user
```


A função input_pattern(), é uma função decoradora que fornece o input para a função decorada enquanto espera que ela 
realize a validação e tratamento do dado fornecido, além disso, realiza a recursividade para dados incorretos e controla
o número de chamadas recursivas realizadas. Ficando assim para as demais funções (input_name(), input_date(), etc)
a responsabilidade de tratar os dados específicos que recebem e sinalizarem para o pattern o dado recebido validado e 
tratado ou None, caso a validação falhe.