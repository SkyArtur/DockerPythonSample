from tests import *
from functions import input_date


class TestCaseInputDate(TestCase):
    def setUp(self) -> None:
        self.input_values = ['31/11/2010', '30/11/2010']
        self.input_patch = patch('builtins.input', side_effect=self.input_values)
        self.mock_input = self.input_patch.start()

    def tearDown(self) -> None:
        self.input_patch.stop()

    @patch('builtins.input', side_effect=['30112010'])
    def test_validar_data_correta_somente_numeros(self, moca_input):
        """Validando entrada de uma data válida, apenas os números."""
        data = input_date('Digite uma data: ')
        self.assertEqual(data, '30/11/2010')

    @patch('builtins.input', side_effect=['30-11-2010'])
    def test_validar_data_correta_somente_hifens(self, moca_input):
        """Validando entrada de data válida, digitada com hífens."""
        data = input_date('Digite uma data: ')
        self.assertEqual(data, '30/11/2010')

    def test_recursividade_data_incorreta(self):
        """Testando a recursividade da função. Ela deve retornar o prompt para o usuário,
        caso ele digite uma data errada"""
        data = input_date('Digite a data: ')
        self.assertEqual(data, '30/11/2010')
        self.assertEqual(self.mock_input.call_count, 2)


