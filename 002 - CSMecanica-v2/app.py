'''
programa principal para abrir tela

Programa App_version4
'''

import gi
from Conexao_Banco import Conexao

gi.require_version('Gtk', '3.0')
from gi.repository import Gtk


class Aplicativo:

    def __init__(self):
        # Acessa o arquivo glade
        self.builder = Gtk.Builder()
        self.builder.add_from_file('tela_glade.glade')
        self.builder.connect_signals(self)

        # Acessa a tela principal
        self.telaPrincipal = self.builder.get_object('id_tela_principal')
        self.telaPrincipal.show()

        # Acesso a tela pesquisa
        self.telapesquisa = self.builder.get_object('tela_pesquisa')
        self.mensagemLocalizar = self.builder.get_object('label_pesquisa')
        self.cod = self.builder.get_object('entry_codigo_pesquisa')

        # Acesso a tela de confirmação
        self.telaConfirmacao = self.builder.get_object('id_tela_confirmacao')
        self.mensagemConfirmacao = self.builder.get_object('mensagem_confirmacao')

        ##tela dialogo
        self.telaDialogo = self.builder.get_object('id_tela_dialogo')

        # atribui as mensagens na tela
        self.mensagem = self.builder.get_object('label_mensagem')
        self.mensagemAviso = "Favor localizar o registro antes."
        self.mensagemAviso1 = 'Favor preencher todos os dados'

        # Tela de abertura onde ira aparecer o logo
        self.logoPrincipal = self.builder.get_object('img_logo')
        self.fixo_home = self.builder.get_object('fixo_home')
        imgLogo = 'img/logo.jpg'
        self.logoPrincipal.set_from_file(imgLogo)
        self.logoPrincipal.show()
        self.fixo_home.set_visible(True)
        self.visitadoHome = True

        # atribui os botoes de insercao de dados
        self.botaoSalvar = self.builder.get_object('btn_salvar')
        self.btnEditar = self.builder.get_object('btn_editar')
        self.btnLocalizar = self.builder.get_object('btn_localizar')
        self.btnExcluir = self.builder.get_object('btn_excluir')
        self.btnCancelar = self.builder.get_object('btn_cancelar')

        # atribuir o grid fixo da tela cliente
        self.fixo_cliente = self.builder.get_object('fixo_cliente')
        self.visitadoCliente = False

        # atribui o grid dos botoes de ediçao
        self.fixo_botoes = self.builder.get_object('fixo_botao')

        # atribui o grid da tela carros
        self.fixo_carros = self.builder.get_object('fixo_carros')
        self.visitadoCarros = False

        # Atribui o gri da tela Manutencao
        self.fixoManutencao = self.builder.get_object('fixo_manutencao')
        self.visitadoManutencao = False

        # atribui treeView

        self.treeviewCarros = self.builder.get_object('treeview_carros')
        self.treeViewManutencao = self.builder.get_object('treeView_manu')

    # Fecha a tela de pesquisa
    def fecharTelaPesquisa(self, widget):
        self.telapesquisa.hide_on_delete()

    def fecharTelaConfirmacao(self, widget):
        self.telaDialogo.destroy()

    # Fecha o programa
    def sairTelaPrincipal(self, widget):
        Gtk.main_quit()

    def main(self):
        Gtk.main()

    ############## Facade #################

    def botaoLadoEsquerdoHome(self, widget):
        if self.visitadoCliente:
            self.fixo_cliente.set_visible(False)
        if self.visitadoCarros:
            self.fixo_carros.set_visible(False)
        if self.visitadoManutencao:
            self.fixoManutencao.set_visible(False)

        logo = self.logoPrincipal
        self.fixo_home.set_visible(True)

        self.fixo_botoes.set_visible(False)
        self.visitadoHome = True

        bo = BusinessBotoesEsquerdoHome(logo, widget)
        abrirHome = bo.botaoHome()

        return abrirHome

    def botaoLadoEsquerdoCliente(self, widget):
        if self.visitadoHome:
            self.fixo_home.set_visible(False)

        if self.visitadoCarros:
            self.fixo_carros.set_visible(False)

        if self.visitadoManutencao:
            self.fixoManutencao.set_visible(False)

        self.fixo_cliente.set_visible(True)
        self.fixo_botoes.set_visible(True)
        self.visitadoCliente = True

        conexao = Conexao()
        builder = self.builder
        mensagem = self.mensagem
        bo = BusinessBotoesEsquerdoCliente(builder, conexao, mensagem, widget)
        abrirCliente = bo.botaoCliente()

        return abrirCliente

    def botaoLadoEsquerdoCarro(self, widget):
        if self.visitadoHome:
            self.fixo_home.set_visible(False)

        if self.visitadoCliente:
            self.fixo_cliente.set_visible(False)

        if self.visitadoManutencao:
            self.fixoManutencao.set_visible(False)

        self.fixo_carros.set_visible(True)
        self.fixo_botoes.set_visible(True)
        self.visitadoCarros = True

        conexao = Conexao()
        mensagem = self.mensagem
        builder = self.builder
        bo = BusinessBotoesEsquerdoCarro(builder, conexao, mensagem, widget)
        abrirCarro = bo.botaoCarros()

        return abrirCarro

    def botaoLadoEsquerdoManutencao(self, widget):
        if self.visitadoHome:
            self.fixo_home.set_visible(False)

        if self.visitadoCliente:
            self.fixo_cliente.set_visible(False)

        if self.visitadoCarros:
            self.fixo_carros.set_visible(False)

        self.fixoManutencao.set_visible(True)
        self.fixo_botoes.set_visible(True)
        self.visitadoManutencao = True

        conexao = Conexao()
        mensagem = self.mensagem
        builder = self.builder
        bo = BusinessBotoesEsquerdoManutencao(builder, conexao, mensagem, widget)
        abrirManutencao = bo.botaoManutencao()

        return abrirManutencao

    ############inserir dados nas tabelas ############

    def inserirDados(self, widget):
        conexao = Conexao()
        builder = self.builder
        mensagem = self.mensagem
        if self.visitadoCliente:
            bo = BusinessBotoesEsquerdoCliente(builder, conexao, mensagem, widget)
            inserirdadosCliente = bo.inserirCliente()

            return inserirdadosCliente

        if self.visitadoCarros:
            bo = BusinessBotoesEsquerdoCarro(builder, conexao, mensagem, widget)
            inserirdadosCarros = bo.inserirCarros()

            return inserirdadosCarros

        if self.visitadoManutencao:
            bo = BusinessBotoesEsquerdoManutencao(builder, conexao, mensagem, widget)

            inserirdadosManutencao = bo.inserirManutencao()

            return inserirdadosManutencao


class BusinessBotoesEsquerdoHome(object):

    def __init__(self, logo, widget):
        self.logo = logo
        self.widget = widget
        imgLogo = 'img/logo.jpg'
        self.logo.set_from_file(imgLogo)

    def botaoHome(self):
        self.logo.show()

        return print('Home')


class BusinessBotoesEsquerdoCliente(object):

    def __init__(self, builder, conexao, mensagem, widget):
        self.builder = builder
        self.conexao = conexao
        self.mensagem = mensagem
        self.mensagemAviso = 'Favor preencher todos os dados'
        self.widget = widget
        self.textNome = self.builder.get_object('entry_nome')
        self.textApelidio = self.builder.get_object('entry_apelidio')
        self.textTelefone = self.builder.get_object('entry_telefone')
        self.textEnd = self.builder.get_object('entry_end')
        self.textNumero = self.builder.get_object('entry_num')
        self.textBairro = self.builder.get_object('entry_bairro')
        self.treeview = self.builder.get_object('treview_cliente')

    def botaoCliente(self):
        self.limparTreeviewCliente()
        self.carregaDadosTreviewCliente()

        return print('Cliente')

    def abrirTelaDialogo(self, msn):
        dialog = Gtk.MessageDialog(None, 0, Gtk.MessageType.INFO,
                                   Gtk.ButtonsType.OK, "Aviso!")
        dialog.format_secondary_text(msn)
        dialog.run()
        print("INFO dialog closed")

        dialog.destroy()

    def inserirCliente(self):

        if self.textNome.get_text() and self.textApelidio.get_text() \
            and self.textNumero.get_text() and self.textBairro.get_text() \
            and self.textTelefone.get_text() != '':

            cliente = self.conexao
            cliente.nome = self.textNome.get_text().upper()
            cliente.apelidio = self.textApelidio.get_text().upper()
            cliente.logadouro = self.textEnd.get_text().upper()
            cliente.numero = self.textNumero.get_text()
            cliente.bairro = self.textBairro.get_text().upper()
            cliente.telefone = self.textTelefone.get_text()
            self.mensagem = self.mensagem.set_text(cliente.inserirDadosCliente())
        else:
            self.abrirTelaDialogo(self.mensagemAviso)

        return self.mensagem

    def carregaDadosTreviewCliente(self):
        cliente = self.conexao

        self.listStore = Gtk.ListStore(int, str, str, str, int, str, str)
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

    def limparTreeviewCliente(self):

        if self.treeview[self.listStore][2]:
            self.mensagem.set_text('')
            self.textNome.set_text('')
            self.textApelidio.set_text('')
            self.textTelefone.set_text('')
            self.textEnd.set_text('')
            self.textNumero.set_text('')
            self.textBairro.set_text('')

            self.treeview.remove_column(self.column_text0)
            self.treeview.remove_column(self.column_text)
            self.treeview.remove_column(self.column_text1)
            self.treeview.remove_column(self.column_text2)
            self.treeview.remove_column(self.column_text3)
            self.treeview.remove_column(self.column_text4)
            self.treeview.remove_column(self.column_text5)


class BusinessBotoesEsquerdoCarro(object):

    def __init__(self, builder, conexao, mensagem, widget):
        self.builder = builder
        self.conexao = conexao
        self.mensagem = mensagem
        self.mensagemAviso = 'Favor preencher todos os dados'
        self.widget = widget
        self.textPlaca = self.builder.get_object('entry_placa')
        self.textTipo = self.builder.get_object('entry_tipo')
        self.textFabricante = self.builder.get_object('entry_fabricante')
        self.textModelo = self.builder.get_object('entry_modelo')
        self.textAno = self.builder.get_object('entry_ano')
        self.textCodCliente = self.builder.get_object('entry_cod_cliente')

    def botaoCarros(self):

        return print('Carros')

    def abrirTelaDialogo(self, msn):
        dialog = Gtk.MessageDialog(None, 0, Gtk.MessageType.INFO,
                                   Gtk.ButtonsType.OK, "Aviso!")
        dialog.format_secondary_text(msn)
        dialog.run()
        print("INFO dialog closed")

        dialog.destroy()

    def inserirCarros(self):
        if self.textPlaca.get_text() != '':
            carros = self.conexao
            carros.placa = self.textPlaca.get_text().upper()
            carros.tipo = self.textTipo.get_text().upper()
            carros.fabricante = self.textFabricante.get_text().upper()
            carros.modelo = self.textModelo.get_text().upper()
            carros.ano = self.textAno.get_text()
            carros.codigo_cliente = self.textCodCliente.get_text()

            self.mensagem.set_text(carros.inserirDadosCarros())

        else:
            self.abrirTelaDialogo(self.mensagemAviso)


class BusinessBotoesEsquerdoManutencao(object):

    def __init__(self, builder, conexao, mensagem, widget):
        self.builder = builder
        self.conexao = conexao
        self.mensagem = mensagem
        self.widget = widget
        self.mensagemAviso = 'Favor preencher todos os dados'
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
        self.cliente_id = 1
        self.carro_id = 1

    def botaoManutencao(self):
        self.comboBoxClienteManu()

        return print('Manutencao')

    def inserirManutencao(self):
        if self.textDataEntrada.get_text() and self.textObs.get_text() and self.textValor.get_text() != '':
            manutencao = self.conexao

            manutencao.data_entrada = str(self.textDataEntrada.get_text())
            manutencao.data_saida = self.textDataSaida.get_text()
            manutencao.defeito = self.textDefeito.get_text(self.textDefeito.get_start_iter(),
                                                           self.textDefeito.get_end_iter(), False).upper()
            manutencao.solucao = self.textSolucao.get_text(self.textSolucao.get_start_iter(),
                                                           self.textSolucao.get_end_iter(), False).upper()
            manutencao.obs = self.textObs.get_text().upper()
            manutencao.valor = self.textValor.get_text()
            manutencao.codigo_carro = self.carro_id
            manutencao.codigo_cliente = self.cliente_id

            manutencao.inserirDadosManutencao()

        else:
            self.abrirTelaDialogo(self.mensagemAviso)

    def comboBoxClienteManu(self):
        manutencao = self.conexao
        self.listStoreComboCliente = Gtk.ListStore(int, str)

        manutencao.comboBoxCliente()
        for linha in manutencao.info:
            self.listStoreComboCliente.append(linha)

        self.textComboxCliente.set_model(self.listStoreComboCliente)
        self.textComboxCliente.connect('changed', self.on_name_combo_changed)
        renderer_text = Gtk.CellRendererText()
        self.textComboxCliente.pack_start(renderer_text, True)
        self.textComboxCliente.add_attribute(renderer_text, "text", 1)

    def on_name_combo_changed(self, combo):
        tree_iter = combo.get_active_iter()
        if tree_iter is not None:
            model = combo.get_model()
            self.cliente_id, name = model[tree_iter][:2]
            self.textComboxCarro.clear()
            self.comboBoxCarroManu(self.cliente_id)
            print(f"Selected: ID={self.cliente_id}, name={name}")

        else:
            entry = combo.get_child()
            print(f"Entered: {entry.get_text()}")

    def comboBoxCarroManu(self, codigo):
        manutencao = self.conexao
        self.listStoreComboCarro = Gtk.ListStore(int, str)

        manutencao.comboBoxCarro(codigo)
        for linha in manutencao.info:
            self.listStoreComboCarro.append(linha)

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
            print(f"Selected: ID={self.carro_id}, name={name}")

        else:
            entry = combo.get_child()
            print("Entered: %s" % entry.get_text())

    def abrirTelaDialogo(self, msn):
        dialog = Gtk.MessageDialog(None, 0, Gtk.MessageType.INFO,
                                   Gtk.ButtonsType.OK, "Aviso!")
        dialog.format_secondary_text(msn)
        dialog.run()
        print("INFO dialog closed")

        dialog.destroy()
