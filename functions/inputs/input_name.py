from .input_pattern import input_pattern


@input_pattern
def input_name(user_input: str) -> str | None:
    """
    Função para validação dos inputs de nomes próprios.
    :param user_input: String comunicando a entrada de texto desejada.
    :return: str('Texto sem Números') | None
    """
    _name = user_input
    if not _name.replace(' ', '').strip().isalpha():
        print(f'ErrorName :: {user_input} :: Não inclua números neste campo!')
        return None
    return _name
