import datetime

from tests import *
from models import ModelPerson


class TestCaseModelPerson(TestCase):
    def setUp(self) -> None:
        self.pessoa = ModelPerson()

    def test_model_person_gen_id_return_int(self):
        self.assertIsInstance(self.pessoa._ModelPerson__gen_id(), int)

    def test_model_person_save(self):
        self.pessoa.first_name = 'Aline'
        self.pessoa.last_name = 'Dantas'
        self.pessoa.birth = '05/11/2000'
        self.pessoa.cpf = '03814212325'
        self.assertTrue(self.pessoa.save())

    def test_model_person_fetchall(self):
        self.assertTrue(self.pessoa.fetchall())

    def test_model_person_fetchone(self):
        self.pessoa.id = 2
        self.assertTrue(self.pessoa.fetchone())
