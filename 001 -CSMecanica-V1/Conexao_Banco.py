'''

programa para manutençao de carros versão 4

conexao com o banco

'''

from banco import Banco


class Conexao(object):

    def __init__(self,codCliente='',nome='',apelidio='',logadouro='',numero='',bairro='',telefone='',
                 codCarros='',tipo='',placa='',fabricante='',modelo='',ano='',codigoCliente='',
                 codManutencao='',dataEntrada='',dataSaida='',defeito='',solucao='',obs='',
                 valor='',codigoCarro=''):

        self.info = []
        self.codCliente = codCliente
        self.nome = nome
        self.apelidio = apelidio
        self.logadouro = logadouro
        self.numero = numero
        self.bairro = bairro
        self.telefone = telefone
        self.codCarros = codCarros
        self.tipo = tipo
        self.placa = placa
        self.fabricante = fabricante
        self.modelo = modelo
        self.ano = ano
        self.codigoCliente = codigoCliente
        self.codManutencao = codManutencao
        self.dataEntrada = dataEntrada
        self.dataSaida = dataSaida
        self.defeito = defeito
        self.solucao = solucao
        self.obs = obs
        self.valor =valor
        self.codigoCarro = codigoCarro

    # cadastra cliente
    def inserirDadosCliente(self):

        banco = Banco()
        try:
            cursor = banco.conexao.cursor()
            cursor.execute('''
                INSERT INTO cliente(Nome,Apelidio,Logadouro,Numero,Bairro,Telefone)
                VALUES (?,?,?,?,?,?)''',
                (self.nome,self.apelidio,self.logadouro,self.numero,self.bairro,self.telefone))

            banco.conexao.commit()
            cursor.close()
            return 'Cadastro efetuado com sucesso '
        except:
            return 'Ocorreu um erro no cadastro'

    # Atualiza dados do cliente
    def atualizarDadosCliente(self):

        banco = Banco()
        try:
            cursor = banco.conexao.cursor()
            cursor.execute('''
                UPDATE cliente SET
                Nome = ?,Apelidio = ?,Logadouro = ?,Numero = ?,Bairro = ?,Telefone = ?
                WHERE CodCliente = ?''',
                (self.nome,self.apelidio,self.logadouro,self.numero,self.bairro,self.telefone,self.codCliente))
            banco.conexao.commit()
            cursor.close()

            return 'Dados atualizados com sucesso'
        except:
            return 'Ocorreu um erro na atualização'

    # Deleta cliente
    def deleteDadosCliente(self,codCliente):

        banco = Banco()
        try:

            cursor = banco.conexao.cursor()

            cursor.execute('''
                DELETE FROM cliente WHERE CodCliente = ?''',
                (codCliente,))

            banco.conexao.commit()
            cursor.close()

            return 'Dados excluido com sucesso'
        except:
            return 'Ocorreu um erro ao tentar excluir'

    def selecionarTudoCliente(self):
        banco = Banco()
        self.info = []
        try:
            cursor = banco.conexao.cursor()
            cursor.execute(
                '''
                SELECT CodCliente,Nome,Apelidio,Logadouro,Numero,Bairro,Telefone
                FROM cliente
                ORDER BY CodCliente
                '''
            )

            for linha in cursor.fetchall():
                self.info.append(linha)
                #print(self.arq)

            cursor.close()

            return 'Pesquisa realizada com sucesso'
        except:
            return 'Ocorreu um erro ao realiza pesquisa'

    def localizarDadosCliente(self,codigo):
        banco = Banco()
        try:
            cursor = banco.conexao.cursor()

            cursor.execute('''
                SELECT * FROM cliente WHERE CodCliente = ?
                 ''', (codigo,))
            for linha in cursor:
                self.nome = linha[1]
                self.apelidio = linha[2]
                self.logadouro = linha[3]
                self.numero = linha[4]
                self.bairro = linha[5]
                self.telefone = linha[6]

            cursor.close()

            return 'Pesquisa realizada com sucesso'
        except:
            return 'Ocorreu erro na pesquisa de dados'

    # Cadastro de carros
    def inserirDadosCarros(self):

        banco = Banco()

        try:
            cursor = banco.conexao.cursor()

            cursor.execute('''
                INSERT INTO carros(Placa,Tipo,Fabricante,Modelo,Ano,CodigoCliente)
                VALUES(?,?,?,?,?,?)''',
                (self.placa,self.tipo,self.fabricante,self.modelo,self.ano,self.codigoCliente))
            banco.conexao.commit()
            cursor.close()

            return 'Cadastro efetuado com sucesso'
        except:
            return 'Ocorreu um erro no cadastro'

    # Atualiza dados do carro
    def atualizarDadosCarros(self):

        banco = Banco()
        try:
            cursor = banco.conexao.cursor()

            cursor.execute('''
                UPDATE carros SET
                Placa = ?,Tipo = ?, Fabricante = ?,Modelo = ?,Ano = ?,CodigoCliente = ?
                WHERE CodCarros = ?''',
                (self.placa,self.tipo,self.fabricante,self.modelo,self.ano,self.codigoCliente,self.codCarros))

            banco.conexao.commit()
            cursor.close()

            return 'Dados atualizados com sucesso'
        except:
            return 'Ocorreu um erro na atualização'

    #seleciona tudo carros
    def selecionaTudoCarros(self):
        banco = Banco()
        self.info = []
        try:
            cursor = banco.conexao.cursor()
            cursor.execute(
                '''
                SELECT CodCarros,Placa,Tipo,Fabricante,Modelo,Ano,CodigoCliente
                FROM carros
                ORDER BY CodCarros
                '''
            )

            for linha in cursor.fetchall():
                self.info.append(linha)

            cursor.close()

            return 'Pesquisa realizada com sucesso'
        except:
            return 'Ocorreu um erro ao realiza pesquisa'

    def localizarDadosCarro(self,codigo):
        banco = Banco()
        try:
            cursor = banco.conexao.cursor()

            cursor.execute('''
                SELECT * FROM carros WHERE CodCarros = ?
                 ''', (codigo,))
            for linha in cursor:
                self.placa = linha[1]
                self.tipo = linha[2]
                self.fabricante = linha[3]
                self.modelo = linha[4]
                self.ano = linha[5]
                self.codigoCliente = linha[6]

            cursor.close()

            return 'Pesquisa realizada com sucesso'
        except:
            return 'Ocorreu erro na pesquisa de dados'

    # Excluir dados de carros
    def deleteDadosCarros(self, codCarros):

        banco = Banco()
        try:
            cursor = banco.conexao.cursor()

            cursor.execute('''
                DELETE FROM carros WHERE codCarros = ?
            ''',(codCarros,))

            banco.conexao.commit()
            cursor.close()

            return 'Dados excluido com sucesso'
        except:
            return 'Ocorreu um erro ao tentar excluir'

    # cadastro manutençao
    def inserirDadosManutencao(self):

        banco = Banco()

        try:
            cursor = banco.conexao.cursor()

            cursor.execute('''
                INSERT INTO manutencao(DataEntrada,DataSaida,Defeito,Solucao,Obs,Valor,CodigoCarro,CodigoCliente)
                VALUES(?,?,?,?,?,?,?,?)''',
                (self.dataEntrada,self.dataSaida,self.defeito,self.solucao,self.obs,
                 self.valor,self.codigoCarro,self.codigoCliente))

            banco.conexao.commit()
            cursor.close()

            return 'Cadastro efetuado com sucesso'
        except:
            return 'Ocorreu um erro no cadastro'

    # Atualizar dados da manutençao

    def atualizarDadosManutencao(self):

        banco = Banco()

        try:
            cursor = banco.conexao.cursor()

            cursor.execute('''
                UPDATE manutencao SET
                DataEntrada = ?,DataSaida = ?,Defeito = ?,Solucao = ?,Obs = ?,Valor = ?,CodigoCarro = ?,CodigoCliente = ?
                WHERE CodManutencao = ?''',
                (self.dataEntrada,self.dataSaida,self.defeito,self.solucao,self.obs,self.valor,
                 self.codigoCarro,self.codigoCliente,self.codManutencao))

            banco.conexao.commit()
            cursor.close()

            return 'Dados atualizados com sucesso'
        except:
            return 'Ocorreu um erro na atualização'

    # Exclui registro de manutenção

    def deleteDadosManutencao(self, codManutencao):

        banco = Banco()

        try:
            cursor = banco.conexao.cursor()

            cursor.execute('''
                DELETE FROM manutencao WHERE CodManutencao = ?
            ''',(codManutencao,))

            banco.conexao.commit()
            cursor.close()

            return 'Dados excluido com sucesso'
        except:
            return 'Ocorreu um erro ao excluir dados'