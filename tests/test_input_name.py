from tests import *
from functions import input_name


class TestCaseInputName(TestCase):
    def setUp(self) -> None:
        self.input_values = ['Aline Santos1', 'Aline Santos']
        self.input_patch = patch('builtins.input', side_effect=self.input_values)
        self.mock_input = self.input_patch.start()

    def tearDown(self) -> None:
        self.input_patch.stop()

    def test_validacao_do_input_do_usuario(self):
        """Teste da chamada recursiva para um nome inválido, seguido de um válido."""
        name = input_name('Digite o nome: ')
        self.assertEqual(name, 'Aline Santos')
        self.assertEqual(self.mock_input.call_count, 2)
