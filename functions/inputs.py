from datetime import date
from re import search


def input_pattern(input_any):
    def _input(label_input: str, __control: int = 5):
        user_input = input_any(input(label_input))
        if not user_input:
            if __control > 0:
                return _input(label_input, __control - 1)
            else:
                raise RuntimeError('Limite da chamadas recursivas.')
        return user_input

    return _input


@input_pattern
def input_name(user_input: str) -> str | bool:
    """Função para validação dos inputs de nomes próprios."""
    _name = user_input
    if not _name.replace(' ', '').strip().isalpha():
        print('Não digite númerais neste campo.')
        return False
    return _name


@input_pattern
def input_date(user_input: str):
    try:
        _date = [int(i) for i in search('^([0-9]{2})/?-?([0-9]{2})/?-?([0-9]{4})$', user_input).groups()]
        _date = date(day=_date[0], month=_date[1], year=_date[2])
    except (ValueError, AttributeError):
        print('Data inválida!')
        return False
    return _date.strftime('%d/%m/%Y')


@input_pattern
def input_numeric(user_input: str, **kwargs):
    try:
        user_input = int(user_input)
    except ValueError:
        print('Valor inválido, somente numerais neste campo!')
        return False
    else:
        return user_input
