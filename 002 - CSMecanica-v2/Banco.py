'''
programa para manutençao de carros versão 4.2

Criação do banco de dados


'''

import sqlite3


class Banco:

    def __init__(self):
        self.conexao = sqlite3.connect('DB_MANUTENCAO.db')
        self.tableCliente()
        self.tableCarro()
        self.tableManutencao()

    def tableCliente(self):
        cursor = self.conexao.cursor()

        cursor.execute('''
                CREATE TABLE if not exists cliente(
                    cod_cliente INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                    nome VARCHAR(50) NOT NULL,
                    apelidio VARCHAR(45),
                    logadouro VARCHAR(50),
                    numero INTEGER(5),
                    bairro VARCHAR(45),
                    telefone VARCHAR(16)     
                 )  

        ''')

        self.conexao.commit()
        cursor.close()

    def tableCarro(self):
        cursor = self.conexao.cursor()

        cursor.execute('''
                CREATE TABLE if not exists carro(
                    cod_carro INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                    placa VARCHAR(10) NOT NULL,
                    tipo VARCHAR(20),
                    fabricante VARCHAR(30),
                    modelo VARCHAR(20),
                    ano INTERGER(4),
                    codigo_cliente INTEGER NOT NULL,
                    FOREIGN KEY (codigo_cliente) REFERENCES cliente(cod_cliente)

                )

        ''')

        self.conexao.commit()
        cursor.close()

    def tableManutencao(self):
        cursor = self.conexao.cursor()

        cursor.execute('''
                CREATE TABLE if not exists manutencao(
                    cod_manutencao INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                    data_entrada DATE,
                    data_saida DATE,
                    defeito TEXT NOT NULL,
                    solucao TEXT,
                    obs TEXT,
                    valor NUMERIC(10,2),
                    codigo_carro INT NOT NULL,
                    codigo_cliente INT NOT NULL,
                    FOREIGN KEY (codigo_carro) REFERENCES carro(codigo_carro),
                    FOREIGN KEY (codigo_cliente) REFERENCES cliente(cod_cliente)                    
                )

        ''')

        self.conexao.commit()
        cursor.close()
