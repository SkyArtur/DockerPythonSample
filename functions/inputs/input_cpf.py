from re import search
from .input_pattern import input_pattern


@input_pattern
def input_cpf(user_input: str) -> str | None:
    """
    Função para validação de entrada do documento CPF.
    :param user_input: String comunicando ao usuário.
    :return: str('000.000.000-00') | None
    """
    try:
        cpf = search('^([0-9]{3})\\.?([0-9]{3})\\.?([0-9]{3})-?([0-9]{2})$', user_input).groups()
        validators_digits = cpf[3]
        validate, check = str(), True
        while check:
            digit, check = 0, True if len(validate) < 1 else False
            for i, j in enumerate(range(10 if check else 11, 1, -1)):
                digit += int(user_input[i]) * j
            digit = 11 - (digit % 11)
            digit = 0 if digit > 9 else digit
            validate += str(digit)
        if not validate == validators_digits:
            raise ValueError
    except (AttributeError, ValueError):
        print(f'ErrorCPF :: {user_input} :: CPF inválido!')
        return None
    else:
        return f'{cpf[0]}.{cpf[1]}.{cpf[2]}-{cpf[3]}'
