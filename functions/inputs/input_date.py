from re import search
from datetime import date
from .input_pattern import input_pattern


@input_pattern
def input_date(user_input: str) -> str | None:
    """
    Função para validação de inputs de datas.
    :param user_input: String comunicando a data desejada.
    :return: str('dd/mm/yyy') | None
    """
    try:
        _date = [int(i) for i in search('^([0-9]{2})/?-?([0-9]{2})/?-?([0-9]{4})$', user_input).groups()]
        _date = date(day=_date[0], month=_date[1], year=_date[2])
    except (ValueError, AttributeError):
        print(f'ErrorDate :: {user_input} :: Data inválida!')
        return None
    return _date.strftime('%d/%m/%Y')
