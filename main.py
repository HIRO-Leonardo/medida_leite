from sistema import *
from database import *

while True:
    
    resposta = menu(['Ver quantidade de leite','Ver tabela, ','Inserir total de leite', 'Ver quando deu no mes', 'Sair'])
    if resposta == 1:
        medida = float(input('Digite em centimetros na regua de medir leite: '))
        verLeite(medida)
        break
    elif resposta == 2:
        Verlista()
        break
    elif resposta == 3:
        while True:
            total_leite = float(input("Digite o total de leite: "))
            adcionarTotalLeite(total_leite)
            resp = str(input("Deseja inserir mais algum dado S/N? ")).upper().split()[0]
            if resp == 'N':
                break
    elif resposta == 4:
        print('Ver quando deu no mes')
        mes = int(input('Digite o mes que voce quer buscar em numeros: '))
        verdadosMes(mes)
        resp = str(input("Deseja ver informar o preco do leite para fazer o total em R$ S/N? ")).upper().split()[0]
        if resp == 'N':
                break
        preco = float(input("Digite o preco do litro do leite: R$"))
        verPreco(preco, mes)
        break
    elif resposta == 5:
        print('Sair')
        break
    else: 
        print('ERRO!!! DIGITE UMA OPCAO VALIDA')


