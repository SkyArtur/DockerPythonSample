from tests import *
from functions import input_cpf


class TestCaseInputCPF(TestCase):
    def setUp(self) -> None:
        self.input_values = ['06347606021', '06347606020']
        self.input_patch = patch('builtins.input', side_effect=self.input_values)
        self.mock_input = self.input_patch.start()

    def tearDown(self) -> None:
        self.input_patch.stop()

    @patch('builtins.input', side_effect=['06347606020'])
    def test_recebendo_cpf_valido_apenas_numeros(self, mock_input):
        """Testando recebendo somente os numeros."""
        cpf = input_cpf('Digite o CPF: ')
        self.assertEqual(cpf, '063.476.060-20')

    def test_verificando_recursividade_e_validacao(self):
        """Verificando a verificação por recursividade."""
        cpf = input_cpf('Digite o CPF: ')
        self.assertEqual(cpf, '063.476.060-20')
        self.assertEqual(self.mock_input.call_count, 2)
