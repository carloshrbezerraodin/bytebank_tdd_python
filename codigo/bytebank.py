from datetime import date
from operator import truediv


class Funcionario:

    def __init__(self, nome, data_nascimento, salario):
        self._nome = nome
        self._data_nascimento = data_nascimento
        self._salario = salario

    @property
    def nome(self):
        return self._nome

    @property
    def salario(self):
        return self._salario

    def idade(self):
        data_nascimento_quebrada = self._data_nascimento.split('/')
        ano_nascimento = data_nascimento_quebrada[-1]
        ano_atual = date.today().year
        return ano_atual - int(ano_nascimento)
        return ano_atual - int(ano_nascimento)

    def sobrenome(self):
        nomme_completo = self.nome.strip()
        nome_quebrado = nomme_completo.split(' ')
        return nome_quebrado[-1]

    def _eh_socio(self):
        sobrenomes = ['Bezerra']
        return (self._salario >= 10000 and (self.sobrenome() in sobrenomes))


    def decrescimo_salario(self):
        if self._eh_socio():
            decrescimo = self._salario * 0.1
            self._salario = self._salario - decrescimo

    def calcular_bonus(self):
        valor = self._salario * 0.1
        if valor > 100:
            raise Exception('O Salario e muito alto para receber um bonus')
        return valor

    def __str__(self):
        return f'Funcionario({self._nome},{self._salario},{self._data_nascimento})'