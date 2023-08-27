def input_pattern(input_any):
    """
    Função Decoradora. Disponibiliza um input para a entrada de dados e espera o tratamento
    destes dados para liberar o usuário de um laço criado por recursividade.
    """

    def _input(label_input: str, __control: int = 5, **kwargs) -> str | float:
        """
        Função interna que realiza o controle de recursividade.
        :param label_input: Label para comunicação do input.
        :param __control: Controla o número de chamadas recursivas da função.
        :return: str | float
        """
        user_input = input_any(input(label_input), **kwargs)
        if user_input is None:
            if __control > 0:
                return _input(label_input, __control - 1, **kwargs)
            else:
                raise RuntimeError('Limite da chamadas recursivas.')
        return user_input
    return _input
