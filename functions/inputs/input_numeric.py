from .input_pattern import input_pattern


@input_pattern
def input_numeric(user_input: str, **kwargs) -> float | None:
    """
    Função para tratamento de valores numéricos. Oferece a possibilidade de controlar
    os valores de entrada, a partir de um mínimo, de um máximo, ou de um intervalo entre
    ambos.
    :param user_input: String comunicando os valores desejados.
    :param kwargs:{minn=Valor mínimo aceitável, maxx=Valor máximo aceitável}.
    :return: float | None
    """
    msg_min, msg_max = None, None
    try:
        _input = float(user_input)
        if kwargs:
            if kwargs.get('minn'):
                msg_min = f'Input({_input}) menor que {kwargs.get("minn")}'
                if _input < kwargs.get('minn'):
                    raise ValueError
            if kwargs.get('maxx'):
                msg_max = f'Input({_input}) maior que {kwargs.get("maxx")}'
                if _input > kwargs.get('maxx'):
                    raise ValueError
    except ValueError:
        print(
            str(f'ErrorNumeric :: {user_input} :: Somente numerais neste campo!'
                f'\n{msg_min if msg_min is not None else ""}'
                f'\n{msg_max if msg_max is not None else ""}'
            ).strip()
        )
        return None
    else:
        return _input
