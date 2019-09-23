'''
programa para manutençao de carros versão 4

Criação do banco de dados


'''

import sqlite3

class Banco:

    def __init__(self):

        self.conexao = sqlite3.connect('DBManutencao.db')
        self.tableCliente()
        self.tableCarros()
        self.tableManutencao()

    def tableCliente(self):

        cursor = self.conexao.cursor()

        cursor.execute('''
                CREATE TABLE if not exists cliente(
                    CodCliente INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                    Nome VARCHAR(50) NOT NULL,
                    Apelidio VARCHAR(45),
                    Logadouro VARCHAR(50),
                    Numero INTEGER(5),
                    Bairro VARCHAR(45),
                    Telefone VARCHAR(16)     
                 )  
                
        ''')

        self.conexao.commit()
        cursor.close()

    def tableCarros(self):

        cursor = self.conexao.cursor()

        cursor.execute('''
                CREATE TABLE if not exists carros(
                    CodCarros INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                    Placa VARCHAR(10) NOT NULL,
                    Tipo VARCHAR(20),
                    Fabricante VARCHAR(30),
                    Modelo VARCHAR(20),
                    Ano INTERGER(4),
                    CodigoCliente INT NOT NULL,
                    FOREIGN KEY (CodigoCliente) REFERENCES cliente(CodCliente)
                
                )
        
        ''')

        self.conexao.commit()
        cursor.close()


    def tableManutencao(self):

        cursor = self.conexao.cursor()

        cursor.execute('''
                CREATE TABLE if not exists manutencao(
                    CodManutencao INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                    DataEntrada DATE NOT NULL,
                    DataSaida DATE,
                    Defeito TEXT NOT NULL,
                    Solucao TEXT,
                    Obs TEXT,
                    Valor NUMERIC(10,2),
                    CodigoCarro INT NOT NULL,
                    CodigoCliente INT NOT NULL,
                    FOREIGN KEY (CodigoCarro) REFERENCES carros(CodigoCarro),
                    FOREIGN KEY (CodigoCliente) REFERENCES cliente(CodCliente)                    
                )
        
        ''')

        self.conexao.commit()
        cursor.close()