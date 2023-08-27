from tests import *
from functions.inputs.input_pattern import input_pattern


@input_pattern
def somente_letras(user_input: str):
    """Implementando uma função simples para validação do input."""
    if not user_input.isalpha():
        return None
    return user_input


class TestCaseInputPattern(TestCase):
    def setUp(self) -> None:
        self.input_values = ['asd1', 'asd2', 'asdf']
        self.input_patch = patch('builtins.input', side_effect=self.input_values)
        self.mock_input = self.input_patch.start()

    def tearDown(self) -> None:
        self.input_patch.stop()

    def test_de_recursividade_para_valores_incorretos(self):
        """Testando a recursividade da função. Ela deve retornar o prompt para o usuário,
        caso ele digite uma entrada inválida."""
        letras = somente_letras('Digite somente letras')
        self.assertEqual(letras, 'asdf')
        self.assertEqual(self.mock_input.call_count, 3)

    def test_recursividade_maxima(self):
        """Testando o limitador de recursividade da função. Ele deve limitar o número de
        chamadas realizadas pela função, por default '__control' está definido em 5,
        para o teste ele foi alterado de forma forçada para 2."""
        data = somente_letras('Digite somente letras: ', __control=2)
        self.assertEqual(data, 'asdf')
        self.assertEqual(self.mock_input.call_count, 3)
        self.assertRaises(RuntimeError)
