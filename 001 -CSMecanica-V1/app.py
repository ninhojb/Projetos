'''
programa principal para abrir tela

Programa App_version4
'''

from Conexao_Banco import Conexao

import gi
gi.require_version('Gtk','3.0')
from gi.repository import Gtk

class Aplicativo:

    def __init__(self):

        #Acessa o arquivo glade
        self.builder = Gtk.Builder()
        self.builder.add_from_file('arq.glade')
        self.builder.connect_signals(self)

        #Acessa a tela principal
        self.telaPrincipal = self.builder.get_object('id_tela_principal')
        self.telaPrincipal.show()

        # Acesso a tela pesquisa
        self.telapesquisa = self.builder.get_object('tela_pesquisa')
        self.mensagemLocalizar = self.builder.get_object('label_pesquisa')
        self.cod = self.builder.get_object('entry_codigo_pesquisa')

        #Acesso a tela de confirmação
        self.telaConfirmacao = self.builder.get_object('id_tela_confirmacao')
        self.mensagemConfirmacao = self.builder.get_object('mensagem_confirmacao')

        ##tela dialogo
        self.telaDialogo = self.builder.get_object('id_tela_dialogo')

        #atribui as mensagens na tela
        self.mensagem = self.builder.get_object('label_mensagem')

        # atribui o grid fixo home e logo
        self.logoPrincipal = self.builder.get_object('img_logo')
        self.fixo_home = self.builder.get_object('fixo_home')
        self.imgLogo = 'img/logo.jpg'
        self.logoPrincipal.set_from_file(self.imgLogo)
        self.logoPrincipal.show()
        self.fixo_home.set_visible(True)
        self.vistaHome = False

        #atribui os botoes de insercao de dados
        self.botaoSalvar = self.builder.get_object('btn_salvar')
        self.btnEditar = self.builder.get_object('btn_editar')
        self.btnLocalizar = self.builder.get_object('btn_localizar')
        self.btnExcluir = self.builder.get_object('btn_excluir')
        self.btnCancelar = self.builder.get_object('btn_cancelar')

        #atribuir o grid fixo da tela cliente
        self.fixo_cliente = self.builder.get_object('fixo_cliente')
        self.visitadoCliente = False
        self.textNome = self.builder.get_object('entry_nome')
        self.textApelidio = self.builder.get_object('entry_apelidio')
        self.textTelefone = self.builder.get_object('entry_telefone')
        self.textEnd = self.builder.get_object('entry_end')
        self.textNumero = self.builder.get_object('entry_num')
        self.textBairro = self.builder.get_object('entry_bairro')

        #atribui o grid dos botoes de ediçao
        self.fixo_botoes = self.builder.get_object('fixo_botao')

        #atribui o grid da tela carros
        self.fixo_carros = self.builder.get_object('fixo_carros')
        self.visitadoCarros = False
        self.textPlaca = self.builder.get_object('entry_placa')
        self.textTipo = self.builder.get_object('entry_tipo')
        self.textFabricante = self.builder.get_object('entry_fabricante')
        self.textModelo = self.builder.get_object('entry_modelo')
        self.textAno = self.builder.get_object('entry_ano')
        self.textCodCliente = self.builder.get_object('entry_cod_cliente')

        #Atribui o gri da tela Manutencao
        self.fixoManutencao = self.builder.get_object('fixo_manutencao')
        self.visitadoManutencao = False
        self.textDataEntrada = self.builder.get_object('entry_entrada')
        self.textDataSaida = self.builder.get_object('entry_saida')
        self.defeitoBuffer = self.builder.get_object('textView_defeito')
        self.textDefeito = self.defeitoBuffer.get_buffer()
        self.solucaoBuffer = self.builder.get_object('textView_solucao')
        self.textSolucao = self.solucaoBuffer.get_buffer()
        self.textObs = self.builder.get_object('entry_obs')
        self.textValor = self.builder.get_object('entry_valor')
        self.textComboxCliente = self.builder.get_object('combox_cliente')
        self.textComboxCarro = self.builder.get_object('combox_carro')

        #atribui treeView
        self.treeview = self.builder.get_object('treview_cliente')
        self.treeviewCarros = self.builder.get_object('treeview_carros')
        self.treeViewManutencao = self.builder.get_object('treeView_manu')

    #Botes do lado esquerdo
    #Botao home
    def botaoHome(self, widget):
        if self.visitadoCliente:
            self.limparTreeviewCliente(widget)
            self.visitadoCliente = False

        if self.visitadoCarros:
            self.limparTreeviewCarros(widget)
            self.visitadoCarros = False

        if self.visitadoManutencao:
            self.limparTreeviewManutencao(widget)
            self.limpaComboxCliente(widget)
            self.visitadoManutencao = False

        if not self.vistaHome:
            self.imgLogo = 'img/logo.jpg'
            self.logoPrincipal.set_from_file(self.imgLogo)
            self.logoPrincipal.show()
            self.fixo_cliente.set_visible(False)
            self.fixo_botoes.set_visible(False)
            self.fixo_carros.set_visible(False)
            self.fixoManutencao.set_visible(False)
            self.fixo_home.set_visible(True)
            self.vistaHome = True
        else:
            pass

    #Botao Clientes
    def botaoCliente(self,widget):
        if self.visitadoCarros:
            self.limparTreeviewCarros(widget)
            self.visitadoCarros = False

        if self.visitadoManutencao:
            self.limparTreeviewManutencao(widget)
            self.limpaComboxCliente(widget)
            self.visitadoManutencao = False

        if self.vistaHome:
            self.vistaHome = False

        if not self.visitadoCliente:
            self.fixo_home.set_visible(False)
            self.fixo_carros.set_visible(False)
            self.fixoManutencao.set_visible(False)
            self.fixo_cliente.set_visible(True)
            self.fixo_botoes.set_visible(True)
            self.carregaDadosTreviewCliente(widget)
            self.limpaMensagemDados(widget)
            self.visitadoCliente = True
        else:
            pass

    #Botao Carros
    def botaoCarros(self,widget):
        if self.visitadoCliente:
            self.limparTreeviewCliente(widget)
            self.visitadoCliente = False

        if self.visitadoManutencao:
            self.limparTreeviewManutencao(widget)
            self.limpaComboxCliente(widget)
            self.visitadoManutencao = False

        if self.vistaHome:
            self.vistaHome = False

        if not self.visitadoCarros:
            self.fixo_home.set_visible(False)
            self.fixo_cliente.set_visible(False)
            self.fixoManutencao.set_visible(False)
            self.fixo_carros.set_visible(True)
            self.fixo_botoes.set_visible(True)
            self.carregaTreviewCarros(widget)
            self.limpaDadosCarros(widget)
            self.mensagem.set_text('')
            self.visitadoCarros = True
        else:
            pass

    def botaoManutencao(self,widget):
        if self.visitadoCliente:
            self.limparTreeviewCliente(widget)
            self.visitadoCliente = False

        if self.visitadoCarros:
            self.limparTreeviewCarros(widget)
            self.visitadoCarros = False

        if self.vistaHome:
            self.vistaHome = False

        if not self.visitadoManutencao:
            self.fixo_home.set_visible(False)
            self.fixo_cliente.set_visible(False)
            self.fixo_carros.set_visible(False)
            self.fixoManutencao.set_visible(True)
            self.fixo_botoes.set_visible(True)
            self.carregaTreviewManutencao(widget)
            self.mensagem.set_text('')
            self.comboBoxClienteManu(widget)
            self.visitadoManutencao = True

        else:
            pass

    #################################################

    #Cadastro de dados do cliente, Carros e manutencao
    def inserirDados(self,widget):
        if self.visitadoCliente:
            if self.textNome.get_text() and self.textApelidio.get_text() \
                and self.textNumero.get_text() and self.textBairro.get_text() \
                and self.textTelefone.get_text() != '':

                cliente = Conexao()
                cliente.nome = self.textNome.get_text().upper()
                cliente.apelidio = self.textApelidio.get_text().upper()
                cliente.logadouro = self.textEnd.get_text().upper()
                cliente.numero = self.textNumero.get_text()
                cliente.bairro = self.textBairro.get_text().upper()
                cliente.telefone = self.textTelefone.get_text()
                self.mensagem.set_text(cliente.inserirDadosCliente())

                self.limpaDadosClientes(widget)
                self.limparTreeviewCliente(widget)
                self.carregaDadosTreviewCliente(widget)
            else:
                self.mensagem.set_text('Favor preencher todos os dados')

        if self.visitadoCarros:
            if self.textPlaca.get_text() and self.textTipo.get_text() and self.textFabricante.get_text()\
                and self.textModelo.get_text() and self.textAno.get_text() and self.textCodCliente.get_text() != '':

                carros = Conexao()
                carros.placa = self.textPlaca.get_text().upper()
                carros.tipo = self.textTipo.get_text().upper()
                carros.fabricante = self.textFabricante.get_text().upper()
                carros.modelo = self.textModelo.get_text().upper()
                carros.ano = self.textAno.get_text()
                carros.codigoCliente = self.textCodCliente.get_text()

                self.mensagem.set_text(carros.inserirDadosCarros())

                self.limpaDadosCarros(widget)
                self.limparTreeviewCarros(widget)
                self.carregaTreviewCarros(widget)
            else:
                self.mensagem.set_text('Favor preencher todos os dados')

        if self.visitadoManutencao:
            if self.textDataEntrada.get_text() and self.textObs.get_text() and self.textValor.get_text()\
                and self.cliente_id and self.carro_id != '':

                manutencao = Conexao()

                manutencao.dataEntrada = self.textDataEntrada.get_text()
                manutencao.dataSaida = self.textDataSaida.get_text()
                manutencao.defeito = self.textDefeito.get_text(self.textDefeito.get_start_iter(),
                                                               self.textDefeito.get_end_iter(),False).upper()
                manutencao.solucao = self.textSolucao.get_text(self.textSolucao.get_start_iter(),
                                                               self.textSolucao.get_end_iter(),False).upper()
                manutencao.obs = self.textObs.get_text().upper()
                manutencao.valor = self.textValor.get_text()
                manutencao.codigoCarro = self.carro_id
                manutencao.codigoCliente = self.cliente_id

                self.mensagem.set_text(manutencao.inserirDadosManutencao())
                self.limparTreeviewManutencao(widget)
                self.limpaDadosManutencao(widget)
                self.carregaTreviewManutencao(widget)
            else:
                self.mensagem.set_text('Favor preencher todos os dados')

    # Monta tela localizar do cliente, Carro e manutencao
    def btnLocalizar(self, widget):
        if self.visitadoCliente:
            self.mensagemLocalizar.set_text('Digite o código do cliente')
            self.cod.set_text('')
            self.telapesquisa.show()

        if self.visitadoCarros:
            self.mensagemLocalizar.set_text('Digite o código do carro')
            self.cod.set_text('')
            self.telapesquisa.show()

        if self.visitadoManutencao:
            self.mensagemLocalizar.set_text('Digite o código da manutenção')
            self.cod.set_text('')
            self.telapesquisa.show()

    # Botao localizar da tela pesquisa
    def botaLocalizarPesquisa(self, widget):
        if self.visitadoCliente:
            codigo = self.cod.get_text()
            self.searchDados(codigo, widget=True)
            self.telapesquisa.hide_on_delete()
            if self.textNome.get_text() == '':
                self.mensagem.set_text('Codigo do cliente não existe')

        if self.visitadoCarros:
            codigo = self.cod.get_text()
            self.searchDados(codigo,widget=True)
            self.telapesquisa.hide_on_delete()
            if self.textPlaca.get_text() == '':
                self.mensagem.set_text('Codigo do carro não existe')

        if self.visitadoManutencao:
            codigo = self.cod.get_text()
            self.searchDados(codigo, widget = True)
            self.telapesquisa.hide_on_delete()
            if self.textDataEntrada.get_text() == '':
                self.mensagem.set_text('Codigo da manutenção não existe')

    # Pesquisa os dados e alimenta a tela cliente, carros e manutencao
    def searchDados(self, codigo, widget):
        if self.visitadoCliente:
            cliente = Conexao()
            self.mensagem.set_text(cliente.localizarDadosCliente(codigo))
            self.textNome.set_text(cliente.nome)
            self.textApelidio.set_text(cliente.apelidio)
            self.textEnd.set_text(cliente.logadouro)
            self.textNumero.set_text(str(cliente.numero))
            self.textBairro.set_text(cliente.bairro)
            self.textTelefone.set_text(cliente.telefone)

        if self.visitadoCarros:
            carros = Conexao()
            self.mensagem.set_text(carros.localizarDadosCarro(codigo))
            self.textPlaca.set_text(carros.placa)
            self.textTipo.set_text(carros.tipo)
            self.textFabricante.set_text(carros.fabricante)
            self.textModelo.set_text(carros.modelo)
            self.textAno.set_text(str(carros.ano))
            self.textCodCliente.set_text(str(carros.codigoCliente))

        if self.visitadoManutencao:
            manutencao = Conexao()
            self.limpaComboxCliente(widget)
            print(manutencao.localizaDadosManutencao(codigo))
            self.textDataEntrada.set_text(manutencao.dataEntrada)
            self.textDataSaida.set_text(manutencao.dataSaida)
            self.textObs.set_text(manutencao.obs)
            self.textValor.set_text(str(manutencao.valor))
            self.textDefeito.set_text(manutencao.defeito)
            self.textSolucao.set_text(manutencao.solucao)
            self.clienteCombobox = manutencao.codigoCliente
            self.carroCombobox = manutencao.codigoCarro

            self.alimentaPesquisaCombox( self.clienteCombobox)
            #print('cliente',self.clienteCombobox,'carro',self.clienteCombobox)


    #Editar dados Clientes, carros e manutencao
    def upadateDados(self,widget):

        if self.visitadoCliente:
            if self.textNome.get_text() and self.textApelidio.get_text() \
                and self.textNumero.get_text() and self.textBairro.get_text() \
                and self.textTelefone.get_text() != '':
                cliente = Conexao()
                cliente.nome = self.textNome.get_text().upper()
                cliente.apelidio = self.textApelidio.get_text().upper()
                cliente.logadouro = self.textEnd.get_text().upper()
                cliente.numero = self.textNumero.get_text()
                cliente.bairro = self.textBairro.get_text().upper()
                cliente.telefone = self.textTelefone.get_text()
                cliente.codCliente = self.cod.get_text()

                self.mensagem.set_text(cliente.atualizarDadosCliente())
                self.limpaDadosClientes(widget)
                self.limparTreeviewCliente(widget)
                self.carregaDadosTreviewCliente(widget)
            else:
                self.mensagem.set_text('Favor localizar o registro para edição')

        if self.visitadoCarros:

            if self.textPlaca.get_text() and self.textTipo.get_text() and \
            self.textFabricante.get_text() and self.textModelo.get_text() and \
            self.textAno.get_text() and self.textCodCliente.get_text() != '':

                carro = Conexao()
                carro.placa = self.textPlaca.get_text().upper()
                carro.tipo = self.textTipo.get_text().upper()
                carro.fabricante = self.textFabricante.get_text().upper()
                carro.modelo = self.textModelo.get_text().upper()
                carro.ano = self.textAno.get_text().upper()
                carro.codigoCliente = self.textCodCliente.get_text()
                carro.codCarros = self.cod.get_text()

                self.mensagem.set_text(carro.atualizarDadosCarros())
                self.limpaDadosCarros(widget)
                self.limparTreeviewCarros(widget)
                self.carregaTreviewCarros(widget)

            else:
                self.mensagem.set_text('Favor localizar o registro para edição')

        if self.visitadoManutencao:
            if self.textDataEntrada and self.carro_id != '':
                manutencao = Conexao()

                manutencao.dataEntrada = self.textDataEntrada.get_text()
                manutencao.dataSaida = self.textDataSaida.get_text()
                manutencao.defeito = self.textDefeito.get_text(self.textDefeito.get_start_iter(),
                                                               self.textDefeito.get_end_iter(), False).upper()
                manutencao.solucao = self.textSolucao.get_text(self.textSolucao.get_start_iter(),
                                                               self.textSolucao.get_end_iter(), False).upper()
                manutencao.obs = self.textObs.get_text().upper()
                manutencao.valor = self.textValor.get_text()
                manutencao.codigoCarro = self.carro_id
                manutencao.codigoCliente = self.cliente_id

                codigo = self.cod.get_text()
                print(manutencao.atualizarDadosManutencao(codigo))

                self.limparTreeviewManutencao(widget)
                self.limpaDadosManutencao(widget)
                self.carregaTreviewManutencao(widget)
            else:
                self.mensagem.set_text('Favor preencher todos os dados')

    #Excluir regstro de cliente, carros e manutencao
    def deleteDados(self,widget):
        if self.visitadoCliente:
            if self.cod.get_text() and self.textNome.get_text() != '':
                cliente = Conexao()
                codigo = self.cod.get_text()
                self.mensagem.set_text(cliente.deleteDadosCliente(codigo))
                self.limpaDadosClientes(widget)
                self.limparTreeviewCliente(widget)
                self.carregaDadosTreviewCliente(widget)
            else:
                self.abrirTelaDialogo(widget)

        if self.visitadoCarros:
            if self.cod.get_text() and self.textPlaca.get_text() != '':
                carros = Conexao()
                codigo = self.cod.get_text()
                self.mensagem.set_text(carros.deleteDadosCarros(codigo))
                self.limpaDadosCarros(widget)
                self.limparTreeviewCarros(widget)
                self.carregaTreviewCarros(widget)
            else:
                self.abrirTelaDialogo(widget)

        if self.visitadoManutencao:
            if self.textDataEntrada.get_text() and self.textValor.get_text() != '':
                manutencao = Conexao()
                codigo = self.cod.get_text()
                print(manutencao.deleteDadosManutencao(codigo))

                self.limparTreeviewManutencao(widget)
                self.limpaDadosManutencao(widget)
                self.carregaTreviewManutencao(widget)
            else:
                self.abrirTelaDialogo(widget)

    def abriTelaConfirmacao(self,widget):

        pass


    def abrirTelaDialogo(self,widget):
        dialog = Gtk.MessageDialog(None, 0, Gtk.MessageType.INFO,
                                   Gtk.ButtonsType.OK, "Aviso!")
        dialog.format_secondary_text(
            "Favor localizar o registro antes.")
        dialog.run()
        print("INFO dialog closed")

        dialog.destroy()


    #Limpa dados do cliente
    def limpaDadosClientes(self,widget):
        self.textNome.set_text('')
        self.textApelidio.set_text('')
        self.textTelefone.set_text('')
        self.textEnd.set_text('')
        self.textNumero.set_text('')
        self.textBairro.set_text('')

    #limpa dados e as mensagens cliente, carros e manutencao
    def limpaMensagemDados(self, widget):
        self.mensagem.set_text('')
        self.limpaDadosClientes(widget)
        self.limpaDadosCarros(widget)
        self.limpaDadosManutencao(widget)

    def limpaDadosCarros(self,widget):
        self.textPlaca.set_text('')
        self.textTipo.set_text('')
        self.textFabricante.set_text('')
        self.textModelo.set_text('')
        self.textAno.set_text('')
        self.textCodCliente.set_text('')

    def limpaDadosManutencao(self,widget):
        self.textDataEntrada.set_text('')
        self.textDataSaida.set_text('')
        self.textObs.set_text('')
        self.textValor.set_text('')
        self.textSolucao.set_text('')
        self.textDefeito.set_text('')
        self.textComboxCliente.clear()
        self.comboBoxClienteManu(widget)

    #limpada o treeView cliente
    def limparTreeviewCliente(self,widget):
        self.treeview.remove_column(self.column_text0)
        self.treeview.remove_column(self.column_text)
        self.treeview.remove_column(self.column_text1)
        self.treeview.remove_column(self.column_text2)
        self.treeview.remove_column(self.column_text3)
        self.treeview.remove_column(self.column_text4)
        self.treeview.remove_column(self.column_text5)

    #Limpa dados Treeview Carros
    def limparTreeviewCarros(self,widget):
        self.treeviewCarros.remove_column(self.column_text0)
        self.treeviewCarros.remove_column(self.column_text)
        self.treeviewCarros.remove_column(self.column_text1)
        self.treeviewCarros.remove_column(self.column_text2)
        self.treeviewCarros.remove_column(self.column_text3)
        self.treeviewCarros.remove_column(self.column_text4)
        self.treeviewCarros.remove_column(self.column_text5)

    def limparTreeviewManutencao(self, widget):
        self.treeViewManutencao.remove_column(self.column_text0)
        self.treeViewManutencao.remove_column(self.column_text)
        self.treeViewManutencao.remove_column(self.column_text1)
        self.treeViewManutencao.remove_column(self.column_text2)
        self.treeViewManutencao.remove_column(self.column_text3)
        self.treeViewManutencao.remove_column(self.column_text4)
        self.treeViewManutencao.remove_column(self.column_text5)
        self.treeViewManutencao.remove_column(self.column_text6)
        self.treeViewManutencao.remove_column(self.column_text7)

    def limpaComboxCliente(self,widget):
        print('limpa Cliente')
        self.textComboxCliente.clear()


    #carrega os dados na tela treview de clientes
    def carregaDadosTreviewCliente(self,widget):
        cliente = Conexao()

        self.listStore = Gtk.ListStore(int,str,str,str,int,str,str)
        self.treeview.set_model(self.listStore)

        renderer_text0 = Gtk.CellRendererText()
        self.column_text0 = Gtk.TreeViewColumn('Codigo', renderer_text0, text=0)
        self.treeview.append_column(self.column_text0)

        renderer_text = Gtk.CellRendererText()
        self.column_text = Gtk.TreeViewColumn('Nome', renderer_text, text=1)
        self.treeview.append_column(self.column_text)

        renderer_text1 = Gtk.CellRendererText()
        self.column_text1 = Gtk.TreeViewColumn('Apelidio', renderer_text1, text=2)
        self.treeview.append_column(self.column_text1)

        renderer_text2 = Gtk.CellRendererText()
        self.column_text2 = Gtk.TreeViewColumn('End', renderer_text2, text=3)
        self.treeview.append_column(self.column_text2)

        renderer_text3 = Gtk.CellRendererText()
        self.column_text3 = Gtk.TreeViewColumn('Numero', renderer_text3, text=4)
        self.treeview.append_column(self.column_text3)

        renderer_text4 = Gtk.CellRendererText()
        self.column_text4 = Gtk.TreeViewColumn('Bairro', renderer_text4, text=5)
        self.treeview.append_column(self.column_text4)

        renderer_text5 = Gtk.CellRendererText()
        self.column_text5 = Gtk.TreeViewColumn('Telefone', renderer_text5, text=6)
        self.treeview.append_column(self.column_text5)

        cliente.selecionarTudoCliente()

        for linha in cliente.info:
            self.listStore.append(linha)

    #Carrega os dados do Treevew Carros
    def carregaTreviewCarros(self, widget):
        carro = Conexao()

        self.listStoreCArros = Gtk.ListStore(int, str, str, str, str, int, int)
        self.treeviewCarros.set_model(self.listStoreCArros)

        renderer_text0 = Gtk.CellRendererText()
        self.column_text0 = Gtk.TreeViewColumn('Codigo', renderer_text0, text=0)
        self.treeviewCarros.append_column(self.column_text0)

        renderer_text = Gtk.CellRendererText()
        self.column_text = Gtk.TreeViewColumn('Placa', renderer_text, text=1)
        self.treeviewCarros.append_column(self.column_text)

        renderer_text1 = Gtk.CellRendererText()
        self.column_text1 = Gtk.TreeViewColumn('Tipo', renderer_text1, text=2)
        self.treeviewCarros.append_column(self.column_text1)

        renderer_text2 = Gtk.CellRendererText()
        self.column_text2 = Gtk.TreeViewColumn('Fabricante', renderer_text2, text=3)
        self.treeviewCarros.append_column(self.column_text2)

        renderer_text3 = Gtk.CellRendererText()
        self.column_text3 = Gtk.TreeViewColumn('Modelo', renderer_text3, text=4)
        self.treeviewCarros.append_column(self.column_text3)

        renderer_text4 = Gtk.CellRendererText()
        self.column_text4 = Gtk.TreeViewColumn('Ano', renderer_text4, text=5)
        self.treeviewCarros.append_column(self.column_text4)

        renderer_text5 = Gtk.CellRendererText()
        self.column_text5 = Gtk.TreeViewColumn('Cliente', renderer_text5, text=6)
        self.treeviewCarros.append_column(self.column_text5)

        carro.selecionaTudoCarros()

        for linha in carro.info:
            self.listStoreCArros.append(linha)

        # Carrega os dados do Treevew Manutencao
    def carregaTreviewManutencao(self, widget):
        manutencao = Conexao()

        self.listStoreanutencao = Gtk.ListStore(int, str, str, str, str, str, float, int,int)

        self.treeViewManutencao.set_model(self.listStoreanutencao)

        renderer_text0 = Gtk.CellRendererText()
        self.column_text0 = Gtk.TreeViewColumn('Codigo', renderer_text0, text=0)
        self.treeViewManutencao.append_column(self.column_text0)

        renderer_text = Gtk.CellRendererText()
        self.column_text = Gtk.TreeViewColumn('Entrada', renderer_text, text=1)
        self.treeViewManutencao.append_column(self.column_text)

        renderer_text1 = Gtk.CellRendererText()
        self.column_text1 = Gtk.TreeViewColumn('Saida', renderer_text1, text=2)
        self.treeViewManutencao.append_column(self.column_text1)

        renderer_text2 = Gtk.CellRendererText()
        self.column_text2 = Gtk.TreeViewColumn('Defeito', renderer_text2, text=3)
        self.treeViewManutencao.append_column(self.column_text2)

        renderer_text3 = Gtk.CellRendererText()
        self.column_text3 = Gtk.TreeViewColumn('Solucao', renderer_text3, text=4)
        self.treeViewManutencao.append_column(self.column_text3)

        renderer_text4 = Gtk.CellRendererText()
        self.column_text4 = Gtk.TreeViewColumn('Obs', renderer_text4, text=5)
        self.treeViewManutencao.append_column(self.column_text4)

        renderer_text5 = Gtk.CellRendererText()
        self.column_text5 = Gtk.TreeViewColumn('Valor', renderer_text5, text=6)
        self.treeViewManutencao.append_column(self.column_text5)

        renderer_text6 = Gtk.CellRendererText()
        self.column_text6 = Gtk.TreeViewColumn('Carro', renderer_text6, text=7)
        self.treeViewManutencao.append_column(self.column_text6)

        renderer_text7 = Gtk.CellRendererText()
        self.column_text7 = Gtk.TreeViewColumn('Cliente', renderer_text7, text=8)
        self.treeViewManutencao.append_column(self.column_text7)

        manutencao.selectTodosDados()

        for linha in manutencao.info:
            self.listStoreanutencao.append(linha)

    ###############################
    #ComboBox

    def comboBoxClienteManu(self, widget):
        manutencao = Conexao()
        self.listStoreComboCliente = Gtk.ListStore(int, str)

        manutencao.comboBoxCliente()
        for linha in manutencao.info:
            self.listStoreComboCliente.append(linha)

        self.textComboxCliente.set_model(self.listStoreComboCliente)
        self.textComboxCliente.connect('changed',self.on_name_combo_changed)
        renderer_text = Gtk.CellRendererText()
        self.textComboxCliente.pack_start(renderer_text, True)
        self.textComboxCliente.add_attribute(renderer_text, "text", 1)

    def on_name_combo_changed(self, combo):
        tree_iter = combo.get_active_iter()
        if tree_iter is not None:
            model = combo.get_model()
            self.cliente_id, self.name = model[tree_iter][:2]
            self.textComboxCarro.clear()
            self.comboBoxCarroManu(self.cliente_id)
            print("Selected: ID=%d, name=%s" % (self.cliente_id, self.name))
        else:
            entry = combo.get_child()
            print("Entered: %s" % entry.get_text())

    def comboBoxCarroManu(self, codigo):
        manutencao = Conexao()
        self.listStoreComboCarro = Gtk.ListStore(int, str)

        manutencao.comboBoxCarro(codigo)
        for linha in manutencao.info:
            self.listStoreComboCarro.append(linha)
            print(linha)

        self.textComboxCarro.set_model(self.listStoreComboCarro)
        self.textComboxCarro.connect('changed', self.on_name_combo_changed_carro)
        renderer_text = Gtk.CellRendererText()
        self.textComboxCarro.pack_start(renderer_text, True)
        self.textComboxCarro.add_attribute(renderer_text, "text", 1)

    def on_name_combo_changed_carro(self, combo):
        tree_iter = combo.get_active_iter()
        if tree_iter is not None:
            model = combo.get_model()
            self.carro_id, name = model[tree_iter][:2]
            print("Selected: ID=%d, name=%s" % (self.carro_id, name))
        else:
            entry = combo.get_child()
            print("Entered: %s" % entry.get_text())

    def alimentaPesquisaCombox(self,id_cliente, widget=True):
        manutencao = Conexao()
        self.listStoreComboCliente = Gtk.ListStore(int, str)

        manutencao.pesquisaNomeCombo(id_cliente)

        for linha in manutencao.info:
            self.listStoreComboCliente.append(linha)

        self.textComboxCliente.set_model(self.listStoreComboCliente)
        renderer_text = Gtk.CellRendererText()
        self.textComboxCliente.pack_start(renderer_text, True)
        self.textComboxCliente.add_attribute(renderer_text, "text", 1)

    # Fecha a tela de pesquisa
    def fecharTelaPesquisa(self, widget):
        self.telapesquisa.hide_on_delete()

    def fecharTelaConfirmacao(self,widget):
        self.telaDialogo.destroy()

    # Fecha o programa
    def sairTelaPrincipal(self, widget):
        Gtk.main_quit()

    def main(self):
        Gtk.main()

if __name__ == '__main__':
    aplicativo = Aplicativo()
    aplicativo.main()