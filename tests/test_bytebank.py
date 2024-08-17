import pytest
from pytest import mark
from codigo.bytebank import Funcionario

class TestClass:
    def test_quanto_idade_recebe_13_04_2_deve_retonar_24(selfs):
        #given
        entrada = '13/03/200'
        esperado = 24

        funcionario_teste = Funcionario('teste', '13/03/2000', 1300)
        #when
        resultado = funcionario_teste.idade()
        #then
        assert resultado == esperado

    def test_quando_sobrenome_recebe_carlos_deve_retonar_bezerra(self):
        entrada = 'Carlos Bezerra'
        esperado = 'Bezerra'
        funcionario_teste = Funcionario(entrada, '13/03/2000', 1300)

        resultado = funcionario_teste.sobrenome()

        assert resultado == esperado

    def test_quando_decrescimo_salario_recebo_10000_deve_retornar_90000(self):

        entrada_salario = 10000
        entrada_nome = 'Bezerra'
        esperado = 9000.0

        funcionario_teste = Funcionario(entrada_nome, '13/03/2000', entrada_salario)
        funcionario_teste.decrescimo_salario()
        resultado = funcionario_teste.salario

        assert resultado == esperado

    @mark.calcular_bonus
    def test_quando_calcular_bonus_receb_1000_deve_retonar_1000(selfs):
        entrada_salario = 1000
        esperado = 100

        funcionario_teste = Funcionario('teste', '13/03/2000', entrada_salario)
        resultado = funcionario_teste.calcular_bonus()
        assert resultado == esperado

    def test_quando_calcular_bonus_recebe_10000000_deve_retornar_exception(selfs):

        with pytest.raises(Exception) :
            entrada_salario = 1100000

            funcionario_teste = Funcionario('teste', '13/03/2000', entrada_salario)
            resultado = funcionario_teste.calcular_bonus()
            assert resultado


    def test_retorno_str(self):
        entrada = 'Carlos Bezerra'
        esperado = 'Funcionario(Carlos Bezerra,1300,13/03/2000)'
        funcionario_teste = Funcionario(entrada, '13/03/2000', 1300)

        resultado = funcionario_teste.__str__()

        assert resultado == esperado