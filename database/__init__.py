import pymysql, pymysql.cursors
from datetime import date, datetime



   

    

def Verlista():
    try:
        conn = pymysql.connect(user={user}, password={password}, host={host}, database={database})
        cursor = conn.cursor()
        query = f'select *from medida_leite ;'
        r = cursor.execute(query)
        data = cursor.fetchall()
    except Exception as error:
        print(f'Deu Algum erro!!!!! {error.__class__},{error.args}')
    else:
        for i in data:
            print(f'ID: {i[0]}, Milimetros: {i[1]} e {i[2]} Litros')
    return data, r

def adcionarTotalLeite(total_leite):
    try:
        horario = datetime.now()
        data_to = date.today()
        conn = pymysql.connect(user={user}, password={password}, host={host}, database={database})
        cursor = conn.cursor()
        query = f"insert into `total_leite` (data, horario, total_leite1)  values (%s, %s, %s);"
        cursor.execute(query, (data_to, horario, total_leite))
        conn.commit()  
    except Exception as error:
        print(f'Deu Algum erro!!!!! {error.__class__},{error.args}')
    else:
        print('Dados cadastrados com sucesso')
    return 

def verdadosMes(mes):
    try:
        conn = pymysql.connect(user={user}, password={password}, host={host}, database={database})
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
    return data, r

def verPreco(preco, mes):
    try:
        conn = pymysql.connect(user={user}, password={password}, host={host}, database={database})
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
        print(f'Preco do litro do leite {preco} * {soma} = R${tot:.2f} ')
    return data, r   
    
def exportarDatabase(mes, preco):
    try:
        data_to = date.today()
        arquivo = open(f"total_de_leite_do_mes_{mes}.txt", 'w+')
        conn = pymysql.connect(user={user}, password={password}, host={host}, database={database})
        cursor = conn.cursor()
        query = f'SELECT * FROM total_leite WHERE month(data) = {mes};'
        r = cursor.execute(query)
        data = cursor.fetchall()
        soma = 0
         
    except Exception as error:
        print(f'Deu Algum erro!!!!! {error.__class__},{error.args}')
    else:
        for i in data:
            print(f'ID:{i[0]}, DATA:{i[1]}, HORARIO: {i[2]} e TOTAL: {i[3]} Litros ')
            arquivo.write(f"ID:{i[0]}, DATA:{1}, HORARIO: {i[2]} e TOTAL: {i[3]} Litros\n")
        for v in data:
            soma += v[3]
        total = soma * preco
        arquivo.write(f"Total do litros de leite no mes {mes}: {soma}.\n")
        arquivo.write(f"Valor do leite: R${preco:.2f}.\n")
        arquivo.write(f"valor do litro do leite e total do leite que foi produzido no mes {mes}: R${total:.2f}.\n")
        arquivo.write(f"arquivo criado no dia {data_to}.")
        return data
