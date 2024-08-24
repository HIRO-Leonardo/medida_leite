from math import trunc
from database import *
import pandas as pd
from sklearn.linear_model import LinearRegression


def cmemmm(cm):
     total = cm * 10
     return trunc(total)

def leiaInt(msg):
     while True:
            try:
               n = int(input(msg))
            except (TypeError, ValueError):
                print('tivemos um problema com o tipo de dado inserido')
                continue
            except (KeyboardInterrupt)      :
               print('O usuario preferiu nao informar os dados')
               return 0 
            else:
                return n

def linha(tam=45):
     return '-'* tam


def cabecalho(txt):
     print(linha())
     print(txt.center(42))
     print(linha())


def menu(lista):
     cabecalho('MENU PRINCIPAL')
     c = 1
     for item in lista:
        print(f'{c} - {item}')
        c += 1
     print(linha())
     opc = leiaInt('Sua Opção: ')
     return opc


