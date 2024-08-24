from sistema import Verlista,menu
from database import verPreco,verdadosMes,exportarDatabase,adcionarTotalLeite
import pandas as pd
from sklearn.linear_model import LinearRegression
from math import trunc

while True:
    resposta=menu(['Ver quantidade de leite','Ver tabela, ','Inserir total de leite', 'Ver quando deu no mes', 'Sair'])
    if resposta == 1:
        medida=float(input('Digite em centimetros na regua de medir leite: '))
        
        total =  medida * 10
        trunc(total)

        df = pd.read_csv("medida_leite.csv")

        modelo = LinearRegression()
        x = df[["Milimetros"]]
        y = df[["Quant_Leite"]]
   
        modelo.fit(x,y)

        milimetros = total 

        if milimetros:
            quant_leite_previsto = modelo.predict([[milimetros]])[0][0] # type: ignore
            print(f'O valor em milimetros: {milimetros:.0f}MM. Equivale-a {quant_leite_previsto:.2f} litros de leite.')
        

    if resposta == 2:
        Verlista()
        break
    if resposta == 3:
        while True:
            total_leite=float(input("Digite o total de leite: "))
            adcionarTotalLeite(total_leite)
            resp = str(input("Deseja inserir mais algum dado S/N? ")).upper().split()[0]
            if resp == 'N':
                break
    if resposta == 4:
        while True:
            print('Ver quando deu no mes')
            mes = int(input('Digite o mes que voce quer buscar em numeros: '))
            verdadosMes(mes)
            resp = str(input("Deseja ver informar o preco do leite para fazer o total em R$ S/N? ")).upper().split()[0]
            if resp == 'N':
                break
            preco = float(input("Digite o preco do litro do leite: R$"))
            verPreco(preco, mes)
            exportar = str(input("Deseja exportar a lista do mes S/N?")).upper().split()[0]
            if resp == 'N':
                break
            exportarDatabase(mes, preco)
            break
    if resposta == 5:
        print('Sair')
        break
