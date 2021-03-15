'''

programa para manutençao de carros versão 4

conexao com o banco

'''

from Banco import Banco


class Conexao(object):

    def __init__(self, cod_cliente='', nome='', apelidio='', logadouro='', numero='', bairro='', telefone='',
                 cod_carro='', tipo='', placa='', fabricante='', modelo='', ano='', codigo_cliente='',
                 cod_manutencao='', data_entrada='', data_saida='', defeito='', solucao='', obs='',
                 valor='', codigo_carro=''):

        self.info = []
        self.cod_cliente = cod_cliente
        self.nome = nome
        self.apelidio = apelidio
        self.logadouro = logadouro
        self.numero = numero
        self.bairro = bairro
        self.telefone = telefone
        self.cod_carro = cod_carro
        self.tipo = tipo
        self.placa = placa
        self.fabricante = fabricante
        self.modelo = modelo
        self.ano = ano
        self.codigo_cliente = codigo_cliente
        self.cod_manutencao = cod_manutencao
        self.data_entrada = data_entrada
        self.data_saida = data_saida
        self.defeito = defeito
        self.solucao = solucao
        self.obs = obs
        self.valor = valor
        self.codigo_carro = codigo_carro

    ########### Cliente ##########################
    def inserirDadosCliente(self):

        banco = Banco()
        try:
            cursor = banco.conexao.cursor()
            cursor.execute('''
                INSERT INTO cliente(
                    Nome,
                    apelidio,
                    logadouro,
                    numero,
                    bairro,
                    telefone
                )
                VALUES (?,?,?,?,?,?)''',
                           (self.nome, self.apelidio, self.logadouro, self.numero, self.bairro, self.telefone))

            banco.conexao.commit()
            cursor.close()
            return 'Cadastro efetuado com sucesso '
        except:
            return 'Ocorreu erro no cadastro'

    # Atualiza dados do cliente
    def atualizarDadosCliente(self):

        banco = Banco()
        try:
            cursor = banco.conexao.cursor()
            cursor.execute('''
                UPDATE cliente SET
                    nome = ?,
                    apelidio = ?,
                    logadouro = ?,
                    numero = ?,
                    bairro = ?,
                    telefone = ?
                WHERE cod_cliente = ?''',
                           (self.nome, self.apelidio, self.logadouro, self.numero, self.bairro, self.telefone,
                            self.cod_cliente))
            banco.conexao.commit()
            cursor.close()

            return 'Dados atualizado com sucesso'
        except:
            return 'Ocorreu erro na atualização'

    # Deleta cliente
    def deleteDadosCliente(self, cod_cliente):

        banco = Banco()
        try:

            cursor = banco.conexao.cursor()

            cursor.execute('''
                DELETE 
                    FROM cliente 
                WHERE cod_cliente = ?''',
                           (cod_cliente,))

            banco.conexao.commit()
            cursor.close()

            return 'Dados excluido com sucesso'
        except:
            return 'Ocorreu erro ao excluir'

    def selecionarTudoCliente(self):
        banco = Banco()
        self.info = []
        try:
            cursor = banco.conexao.cursor()
            cursor.execute(
                '''
                SELECT 
                    cod_cliente,
                    nome,
                    apelidio,
                    logadouro,
                    numero,
                    bairro,
                    telefone
                FROM cliente
                ORDER BY cod_cliente
                '''
            )

            for linha in cursor.fetchall():
                self.info.append(linha)

            cursor.close()

            return 'Pesquisa realizada com sucesso'
        except:
            return 'Ocorreu erro ao realizar pesquisa'

    def localizarDadosCliente(self, codigo):
        banco = Banco()
        try:
            cursor = banco.conexao.cursor()

            cursor.execute('''
                SELECT 
                    * 
                FROM cliente 
                WHERE cod_cliente = ?
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

    ########### Carros ##########################
    def inserirDadosCarros(self):

        banco = Banco()

        try:
            cursor = banco.conexao.cursor()

            cursor.execute('''
                INSERT INTO carro(
                    placa,
                    tipo,
                    fabricante,
                    modelo,
                    ano,
                    codigo_cliente)
                VALUES(?,?,?,?,?,?)''',
                           (self.placa, self.tipo, self.fabricante, self.modelo, self.ano, self.codigo_cliente))
            banco.conexao.commit()
            cursor.close()

            return 'Cadastro efetuado com sucesso'
        except:
            return 'Ocorreu erro no cadastro'

    # Atualiza dados do carro
    def atualizarDadosCarros(self):

        banco = Banco()
        try:
            cursor = banco.conexao.cursor()

            cursor.execute('''
                UPDATE carro SET
                    placa = ?,
                    tipo = ?, 
                    fabricante = ?,
                    modelo = ?,
                    ano = ?,
                    codigo_cliente = ?
                WHERE cod_carros = ?''',
                           (self.placa, self.tipo, self.fabricante, self.modelo, self.ano, self.codigo_cliente,
                            self.cod_carro))

            banco.conexao.commit()
            cursor.close()

            return 'Dados atualizado com sucesso'
        except:
            return 'Ocorreu erro na atualização'

    # seleciona tudo carros
    def selecionaTudoCarros(self):
        banco = Banco()
        self.info = []
        try:
            cursor = banco.conexao.cursor()
            cursor.execute(
                '''
                SELECT 
                    cod_carro,
                    placa,
                    tipo,
                    fabricante,
                    modelo,
                    ano,
                    codigo_cliente
                FROM carro
                ORDER BY cod_carro
                '''
            )

            for linha in cursor.fetchall():
                self.info.append(linha)

            cursor.close()

            return 'Pesquisa realizada com sucesso'
        except:
            return 'Ocorreu erro ao realizar pesquisa'

    def localizarDadosCarro(self, codigo):
        banco = Banco()
        try:
            cursor = banco.conexao.cursor()

            cursor.execute('''
                SELECT 
                    * 
                FROM carro 
                WHERE cod_carro = ?
                 ''', (codigo,))
            for linha in cursor:
                self.placa = linha[1]
                self.tipo = linha[2]
                self.fabricante = linha[3]
                self.modelo = linha[4]
                self.ano = linha[5]
                self.codigo_cliente = linha[6]

            cursor.close()

            return 'Pesquisa realizada com sucesso'
        except:
            return 'Ocorreu erro na pesquisa de dados'

    # Excluir dados de carros
    def deleteDadosCarros(self, cod_carros):

        banco = Banco()
        try:
            cursor = banco.conexao.cursor()

            cursor.execute('''
                DELETE 
                FROM carro
                WHERE cod_carro = ?
            ''', (cod_carros,))

            banco.conexao.commit()
            cursor.close()

            return 'Dados excluido com sucesso'
        except:
            return 'Ocorreu um erro ao tentar excluir'

    ########### Manutencao ##########################

    def inserirDadosManutencao(self):

        banco = Banco()

        # try:
        cursor = banco.conexao.cursor()

        cursor.execute('''
            INSERT INTO manutencao(
                data_entrada,
                data_saida,
                defeito,
                solucao,
                obs,
                valor,
                codigo_carro,
                codigo_cliente)
            VALUES(?,?,?,?,?,?,?,?)''',
                       (self.data_entrada, self.data_saida, self.defeito, self.solucao, self.obs, self.valor,
                        self.codigo_carro, self.codigo_cliente))

        banco.conexao.commit()
        cursor.close()

        #     return 'Cadastro efetuado com sucesso'
        # except:
        #     return 'Ocorreu erro no cadastro'

    def atualizarDadosManutencao(self, codigo):

        banco = Banco()

        try:
            cursor = banco.conexao.cursor()

            cursor.execute('''
                UPDATE manutencao SET
                    data_entrada = ?,
                    data_saida = ?,
                    defeito = ?,
                    solucao = ?,
                    obs = ?,
                    valor = ?,
                    codigo_carro = ?,
                    codigo_cliente = ?
                WHERE cod_manutencao = ?''',
                           (self.data_entrada, self.data_saida, self.defeito, self.solucao, self.obs, self.valor,
                            self.codigo_carro, self.codigo_cliente, codigo))

            banco.conexao.commit()
            cursor.close()

            return 'Dados atualizado com sucesso'
        except:
            return 'Ocorreu erro na atualização'

    def deleteDadosManutencao(self, cod_manutencao):

        banco = Banco()

        try:
            cursor = banco.conexao.cursor()

            cursor.execute('''
                DELETE 
                FROM manutencao 
                WHERE cod_manutencao = ?
            ''', (cod_manutencao,))

            banco.conexao.commit()
            cursor.close()

            return 'Dados excluido com sucesso'
        except:
            return 'Ocorreu erro ao excluir os dados'

    def localizaDadosManutencao(self, codigo):
        banco = Banco()

        try:
            cursor = banco.conexao.cursor()
            cursor.execute(
                '''
                SELECT 
                    * 
                FROM manutencao 
                WHERE cod_manutencao = ?
                ''', (codigo,))

            for linha in cursor:
                self.data_entrada = linha[1]
                self.data_saida = linha[2]
                self.defeito = linha[3]
                self.solucao = linha[4]
                self.obs = linha[5]
                self.valor = linha[6]
                self.codigo_carro = linha[7]
                self.codigo_cliente = linha[8]

            cursor.close()

            return 'Pesquisa realizada com sucesso'
        except:
            return 'Ocorreu erro na pesquisa'

    def selectTodosDados(self, ):
        banco = Banco()
        self.info = []
        try:
            cursor = banco.conexao.cursor()
            cursor.execute(
                '''
                SELECT cod_manutencao,
                    data_entrada,
                    data_saida,
                    defeito,
                    solucao,
                    obs,
                    valor,
                    codigo_carro,
                    codigo_cliente
                FROM manutencao
                ORDER BY cod_manutencao
                '''
            )

            for linha in cursor.fetchall():
                self.info.append(linha)

            cursor.close()

            return 'Pesquisa realizada com sucesso'
        except:
            return 'Ocorreu erro ao realizar pesquisa'

    def comboBoxCliente(self):
        self.info = []
        banco = Banco()

        cursor = banco.conexao.cursor()
        cursor.execute(
            '''
            SELECT 
                cod_cliente, 
                nome
            FROM cliente
            ORDER BY cod_cliente

            '''
        )
        for linha in cursor.fetchall():
            self.info.append(linha)

        cursor.close()

    def comboBoxCarro(self, codigo):
        self.info = []
        banco = Banco()

        cursor = banco.conexao.cursor()
        cursor.execute(
            '''
            SELECT 
                C.cod_carro, 
                C.modelo
            FROM carro AS C
                JOIN cliente AS CL
                    on C.codigo_cliente = CL.cod_cliente 
            WHERE  CL.cod_cliente = ?
            ORDER BY C.modelo

            ''', (codigo,))

        for linha in cursor.fetchall():
            self.info.append(linha)

        cursor.close()

    def pesquisaNomeCombo(self, codigo):
        banco = Banco()
        self.info = []
        cursor = banco.conexao.cursor()

        cursor.execute(
            '''
            SELECT 
                cod_cliente,
                nome
            FROM cliente
            WHERE cod_cliente = ?
            ''', (codigo,))

        for linha in cursor.fetchall():
            self.info.append(linha)
