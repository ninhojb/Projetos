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

        #atribui treeView
        self.treeview = self.builder.get_object('treview_cliente')
        self.treeviewCarros = self.builder.get_object('treeview_carros')

    #Botes do lado esquerdo
    #Botao home
    def botaoHome(self, widget):
        if not self.vistaHome:
            self.imgLogo = 'img/logo.jpg'
            self.logoPrincipal.set_from_file(self.imgLogo)
            self.logoPrincipal.show()
            self.fixo_cliente.set_visible(False)
            self.fixo_botoes.set_visible(False)
            self.fixo_carros.set_visible(False)
            self.fixo_home.set_visible(True)

            if self.visitadoCliente:
                self.limparTreeviewCliente(widget)
                self.visitadoCliente = False

            if self.visitadoCarros:
                self.limparTreeviewCarros(widget)
                self.visitadoCarros = False

            self.vistaHome = True

        else:

            pass

    #Botao Clientes
    def botaoCliente(self,widget):
        if self.visitadoCarros:
            self.limparTreeviewCarros(widget)
            self.visitadoCarros = False

        if not self.visitadoCliente:
            self.fixo_home.set_visible(False)
            self.fixo_carros.set_visible(False)
            self.fixo_cliente.set_visible(True)
            self.fixo_botoes.set_visible(True)
            self.carregaDadosTreviewCliente(widget)
            self.limpaMensagemDados(widget)

            if self.vistaHome:
                self.vistaHome = False

            self.visitadoCliente = True

        else:
            pass

    #Botao Carros
    def botaoCarros(self,widget):

        if not self.visitadoCarros:
            if self.visitadoCliente:
                self.limparTreeviewCliente(widget)
                self.visitadoCliente = False

            self.fixo_home.set_visible(False)
            self.fixo_cliente.set_visible(False)
            self.fixo_carros.set_visible(True)
            self.fixo_botoes.set_visible(True)
            self.carregaTreviewCarros(widget)
            self.limpaDadosCarros(widget)
            self.mensagem.set_text('')

            if self.vistaHome:
                self.vistaHome = False

            self.visitadoCarros = True

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
                self.mensagem.set_text('Codigo do cliente não existe')

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
                self.mensagem.set_text('Favor localizar o registro antes da exclução')

        if self.visitadoCarros:
            if self.cod.get_text() and self.textPlaca.get_text() != '':
                carros = Conexao()
                codigo = self.cod.get_text()
                self.mensagem.set_text(carros.deleteDadosCarros(codigo))
                self.limpaDadosCarros(widget)
                self.limparTreeviewCarros(widget)
                self.carregaTreviewCarros(widget)
            else:
                self.mensagem.set_text('Favor localizar o registro antes da exclusão')

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

    def limpaDadosCarros(self,widget):
        self.textPlaca.set_text('')
        self.textTipo.set_text('')
        self.textFabricante.set_text('')
        self.textModelo.set_text('')
        self.textAno.set_text('')
        self.textCodCliente.set_text('')

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


    # Fecha a tela de pesquisa
    def fecharTelaPesquisa(self, widget):
        self.telapesquisa.hide_on_delete()

    # Fecha o programa
    def sairTelaPrincipal(self, widget):
        Gtk.main_quit()

    def main(self):
        Gtk.main()

if __name__ == '__main__':
    aplicativo = Aplicativo()
    aplicativo.main()