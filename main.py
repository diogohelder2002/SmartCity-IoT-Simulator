import random
import time
from datetime import datetime
import sqlite3


Locais = ["Rua da Boavista", "Aliados", "Alameda senhor da pedra"]
nome_db = "dados_cidade.db"

def base_dados():

    conexao = sqlite3.connect(nome_db)

    cursor = conexao.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS leituras (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            data_hora TEXT,
            local TEXT,
            n_carros INTEGER
        )
    ''')


    conexao.commit()
    conexao.close()

def leitura(nome_da_rua):
    #define a hora
    hora = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    #define o numero de carros que passam
    ncarros = random.randint(0, 5)

    return {
        
        "hora": hora,
        "local": nome_da_rua,
        "carros": ncarros


    }


def guardar_leitura(dados):
    
    conexao = sqlite3.connect(nome_db)
    cursor = conexao.cursor()
    cursor.execute(
        "INSERT INTO leituras (data_hora, local, n_carros) VALUES (?, ?, ?)", 
        (dados['hora'], dados['local'], dados['carros'])
    )
    conexao.commit()
    conexao.close()


def main():
    base_dados()

    try:
        while True:
            for rua in Locais:
                dados = leitura(rua)
                guardar_leitura(dados)

                time.sleep(2)

    except KeyboardInterrupt:
        print("operação interrompida")



if __name__ == "__main__":
    main()