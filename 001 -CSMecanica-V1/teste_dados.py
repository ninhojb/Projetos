from Conexao_Banco import Conexao
#
# #Inserir dados do Cliente
# #
# # dados = Conexao()
# #
# # dados.nome = 'Ne'
# # dados.apelidio = 'ned'
# # dados.logadouro ='Rua Ma'
# # dados.numero = 256
# # dados.bairro = 'Jardim das Flores'
# # dados.telefone = '11 91111'
# #
# #
# # print(dados.inserirDadosCliente())
#
# #inserir dados do Carro
# carros = Conexao()
#
# carros.placa = 'FAB-2527'
# carros.tipo = 'carro'
# carros.fabricante = 'CHEVROLET'
# carros.modelo = 'CAMARO'
# carros.ano = '2011'
# carros.codigoCliente = 1
#
# print(carros.inserirDadosCarros())

#inserir dados da Manutenção
#
# manutencao = Conexao()
#
# manutencao.dataEntrada = '30/09/2019'
# manutencao.dataSaida = '01/10/2019'
# manutencao.defeito = 'Pneus'
# manutencao.solucao = 'Troca do Pneus'
# manutencao.obs = 'Pago'
# manutencao.valor = 50.30
# manutencao.codigoCarro = 1
# manutencao.codigoCliente = 1
#
# print(manutencao.inserirDadosManutencao())


#atualizar dados do cliente

# dados = Conexao()
# dados.nome = 'Fabiana'
# dados.apelidio = 'Fabi'
# dados.logadouro ='Rua Manaca'
# dados.numero = 256
# dados.bairro = 'Vila Anastacia'
# dados.telefone1 = '11 91111-1526'
# dados.telefone2 = '11 92222-5858'
# dados.codCliente = 3
# print(dados.atualizarDadosCliente())

#
# #Atualizar dados do carro
# carros = Conexao()
#
# carros.placa = 'QWE-1234'
# carros.tipo ='astra'
# carros.fabricante = 'CHEVROLET'
# carros.modelo = 'CAMARO'
# carros.ano =2011
# carros.codigoCliente = 2
# carros.codCarros = 2
#
# print(carros.atualizarDadosCarros())

# atualizar dados da manutencao
# manutencao = Conexao()
#
# manutencao.dataEntrada = '30/07/2019'
# manutencao.dataSaida = '01/08/2019'
# manutencao.defeito = 'Oleo'
# manutencao.solucao = 'Troca do oleo'
# manutencao.obs = 'feito em 3 vezez , pago uma'
# manutencao.valor = 100.30
# manutencao.codigoCarro = 1
# manutencao.codigoCliente = 4
# manutencao.codManutencao = 2
# print(manutencao.atualizarDadosManutencao())

#Excluir registro do cliente
# clientes = Conexao()
# codCodigo = 3
#
# print(clientes.deleteDadosCliente(codCodigo))

# Excluir registro de carros

# carros = Conexao()
# codCarros = 2
#
# print(carros.deleteDadosCarros(codCarros))

# Ecluir registro de manutençao
# manutencao = Conexao()
#
# codManutencao = 2
#
#
# print(manutencao.deleteDadosManutencao(codManutencao))
#
#
# manu = Conexao()
#
# manu.comboBoxCarro()
