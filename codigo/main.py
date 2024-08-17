from codigo.bytebank import Funcionario

lucas = Funcionario('Lucas', '13/03/2000', 1000)
print(lucas.idade())


def teste_idade():
    funcionario_teste = Funcionario('teste', '13/03/2000', 1300)
    print(f'Teste = {funcionario_teste.idade()}')

teste_idade()