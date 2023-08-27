from tests import *
from functions import input_numeric


class TestCaseInputNumeric(TestCase):
    def setUp(self) -> None:
        self.input_values = ['1a', '3', '5', '1']
        self.input_patch = patch('builtins.input', side_effect=self.input_values)
        self.mock_input = self.input_patch.start()

    def tearDown(self) -> None:
        self.input_patch.stop()

    @patch('builtins.input', side_effect=['2'])
    def test_retorna_tipo_float(self, mock_input):
        """Testando o typecasting do tipo string, para o tipo float."""
        numero = input_numeric('Digite um numero: ')
        self.assertIsInstance(numero, float)

    @patch('builtins.input', side_effect=['1'])
    def test_retorna_valor_numerico(self, mock_input):
        """Verificando se o retorno pode ser comparado com um tipo inteiro
        de igual valor."""
        numero = input_numeric('Digite um numero: ')
        self.assertEqual(numero, 1)

    @patch('builtins.input', side_effect=['0'])
    def test_retorna_valor_reconhecido_como_bool(self, mock_input):
        """Verificando se o retorno pode ser comparado com um tipo booleano."""
        numero = input_numeric('Digite um numero: ')
        self.assertEqual(numero, False)

    def test_recursividade_para_entrada_de_letras(self):
        numero = input_numeric('Digite um número: ')
        self.assertEqual(numero, 3)
        self.assertEqual(self.mock_input.call_count, 2)

    def test_recursividade_para_valor_menor_que_minn(self):
        numero = input_numeric('Digite um número: ', minn=4)
        self.assertEqual(numero, 5)
        self.assertEqual(self.mock_input.call_count, 3)

    def test_recursividade_para_valor_maior_que_maxx(self):
        numero = input_numeric('Digite um número: ', maxx=2)
        self.assertEqual(numero, 1)
        self.assertEqual(self.mock_input.call_count, 4)

    def test_recursividade_para_valor_entre_minn_e_maxx(self):
        numero = input_numeric('Digite um número: ', minn=1,  maxx=2)
        self.assertEqual(numero, 1)
        self.assertEqual(self.mock_input.call_count, 4)
