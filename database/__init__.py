import pymysql, pymysql.cursors
from datetime import date, datetime


def conexaoBanco(Milimetros=45,):
    try:
        conn = pymysql.connect(user='root', password='', host='localhost', database='leite')
        cursor = conn.cursor()
        query = f'select * from medida_leite where Milimetros = {Milimetros} ;'
        r = cursor.execute(query)
        data = cursor.fetchall()
    except Exception as error:
        print(f'Deu Algum erro!!!!! {error.__class__},{error.args}')
    else:
        for i in data:
            print(f'{i[2]} Litros')
        conn.close()
    return data, r


def Verlista():
    try:
        conn = pymysql.connect(user='root', password='', host='localhost', database='leite')
        cursor = conn.cursor()
        query = f'select *from medida_leite ;'
        r = cursor.execute(query)
        data = cursor.fetchall()
    except Exception as error:
        print(f'Deu Algum erro!!!!! {error.__class__},{error.args}')
    else:
        for i in data:
            print(f'ID: {i[0]}, Milimetros: {i[1]} e {i[2]} Litros')
        conn.close()
    return data, r


def adcionarTotalLeite(total_leite):
    try:
        horario = datetime.now()
        data_to = date.today()
        conn = pymysql.connect(user='root', password='', host='localhost', database='leite')
        cursor = conn.cursor()
        query = f"insert into `total_leite` (data, horario, total_leite1)  values (%s, %s, %s);"
        cursor.execute(query, (data_to, horario, total_leite))
        conn.commit()  
    except Exception as error:
        print(f'Deu Algum erro!!!!! {error.__class__},{error.args}')
    else:
        print('Dados cadastrados com sucesso')
        conn.close()
    return 

def verdadosMes(mes):
    try:
        conn = pymysql.connect(user='root', password='', host='localhost', database='leite')
        cursor = conn.cursor()
        query = f'SELECT * FROM total_leite WHERE month(data) = {mes};'
        r = cursor.execute(query)
        data = cursor.fetchall()
        soma = 0 
    except Exception as error:
        print(f'Deu Algum erro!!!!! {error.__class__},{error.args}')
    else:
        for i in data:
            print(f'ID: {i[0]}, DATA: {i[1]}, HORARIO: {i[2]} e TOTAL: {i[3]} Litros')
            soma += i[3]
        print(f'Total da soma: {soma}')
        conn.close()
    return data, r

def verPreco(preco, mes):
    try:
        conn = pymysql.connect(user='root', password='', host='localhost', database='leite')
        cursor = conn.cursor()
        query = f'SELECT * FROM total_leite WHERE month(data) = {mes};'
        r = cursor.execute(query)
        data = cursor.fetchall()
        soma = 0 
        tot = 0
    except Exception as error:
        print(f'Deu Algum erro!!!!! {error.__class__},{error.args}')
    else:
        for i in data:
            print(f'ID: {i[0]}, DATA: {i[1]}, HORARIO: {i[2]} e TOTAL: {i[3]} Litros')
            soma += i[3]
            
        tot = soma * preco
    
        
        print(f'Total da soma: {soma}')
        print(f'Preco do litro do leite {preco} * {soma} = R${tot} ')
        conn.close()
    return data, r
    
    
