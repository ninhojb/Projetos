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

        #vericar o formulario que esta aberto
        self.verificadorTela = 0
        self.cliqueCliente = True
        self.cliqueHome = True
        self.cliqueCarro = True

        #Acessa o arquivo glade
        self.builder = Gtk.Builder()
        self.builder.add_from_file('arq_version4.glade')
        self.builder.connect_signals(self)

        #Acessa a tela principal
        self.telaPrincipal = self.builder.get_object('id_tela_principal')
        self.telaPrincipal.show()

        #Acesso a tela pesquisa
        self.telapesquisa = self.builder.get_object('tela_pesquisa')
        self.mensagemLocalizar = self.builder.get_object('label_pesquisa')
        self.cod = self.builder.get_object('entry_codigo_pesquisa')

        #mostra o logo principal
        self.logoPrincipal = self.builder.get_object('img_logo')
        imagem = 'img/logo.jpg'
        self.logoPrincipal.set_from_file(imagem)
        self.logoPrincipal.show()

        #Mensagem principal
        self.mensagem = self.builder.get_object('label_mensagem')

        #Formulario de cadastro de cliente
        self.gridCliente = self.builder.get_object('grid_cliente')
        self.treeview = self.builder.get_object('treview_cliente')
        self.frameCliente = self.builder.get_object('frame_cliente')
        self.labelTitulo = self.builder.get_object('label_titulo')
        self.textNome = self.builder.get_object('entry_nome')
        self.textApelidio = self.builder.get_object('entry_apelidio')
        self.textTelefone = self.builder.get_object('entry_telefone')
        self.textEnd = self.builder.get_object('entry_end')
        self.textNumero = self.builder.get_object('entry_numero')
        self.textBairro = self.builder.get_object('entry_bairro')
        self.labelFrame = self.builder.get_object('label_frame')

        #Botoes da horizontal
        self.btnSalvar = self.builder.get_object('btn_salvar')
        self.btnEditar = self.builder.get_object('btn_editar')
        self.btnLocalizar = self.builder.get_object('btn_localizar')
        self.btnExcluir = self.builder.get_object('btn_excluir')
        self.btnCancelar = self.builder.get_object('btn_cancelar')

    #Volta para a tela inicial
    def botaoHome(self,widget):
        self.cliqueCliente = True
        if self.cliqueHome:
            self.logoPrincipal = self.builder.get_object('img_logo')
            imagem = 'img/logo.jpg'
            self.logoPrincipal.set_from_file(imagem)
            self.logoPrincipal.show()
        else:
            self.limpaTelaCliente(widget)
            self.logoPrincipal = self.builder.get_object('img_logo')
            imagem = 'img/logo.jpg'
            self.logoPrincipal.set_from_file(imagem)
            self.cliqueHome = True
            self.logoPrincipal.show()

    #Monta tela de cadastro de  Cliente
    def botaoCliente(self,widget):
        self.verificadorTela = 1
        self.cliqueHome = False
        if self.cliqueCliente:
            self.limpaTelaHome(widget)
            self.labelTitulo.set_text('Cadastro de clientes')
            self.labelFrame.set_text('Clientes:')
            self.gridCliente.set_visible(True)
            self.frameCliente.set_visible(True)
            self.carregaDadosTreview(widget)
            self.mostrarBtn(widget)
            self.cliqueCliente = False
        else:
            self.limparTreeview(widget)
            self.labelTitulo.set_text('Cadastro de clientes')
            self.labelFrame.set_text('Clientes:')
            self.gridCliente.set_visible(True)
            self.frameCliente.set_visible(True)
            self.carregaDadosTreview(widget)
            self.mostrarBtn(widget)

    def botaoCarro(self,widget):
        self.verificadorTela = 2
        self.cliqueHome = False
        self.cliqueCliente = True
        if self.cliqueCarro:
            self.limpaTelaHome(widget)
            self.limpaTelaCliente(widget)
            self.cliqueCarro = False
        else:
            self.limpaTelaHome(widget)

    #inseri dados conforme a varial verificaçao
    #1 formulario de cliente
    #2 formulario de carros
    #3 formulario de manutencao
    def insertDados(self,widget):
        if self.verificadorTela == 1:
            if self.textNome.get_text() and self.textApelidio.get_text()\
                and self.textNumero.get_text() and self.textBairro.get_text()\
                and self.textTelefone.get_text()!= '':
                cliente = Conexao()
                cliente.nome = self.textNome.get_text().upper()
                cliente.apelidio = self.textApelidio.get_text().upper()
                cliente.logadouro = self.textEnd.get_text().upper()
                cliente.numero = self.textNumero.get_text()
                cliente.bairro = self.textBairro.get_text().upper()
                cliente.telefone = self.textTelefone.get_text()

                self.mensagem.set_text(cliente.inserirDadosCliente())
                self.limpaDadosClientes(widget)
                self.limparTreeview(widget)
                self.carregaDadosTreview(widget)
            else:
                self.mensagem.set_text('Campo com (*) é obrigatório')

    #Monta tela localizar do cliente
    def btnLocalizar(self,widget):
        self.telapesquisa.show()
        self.mensagemLocalizar.set_text('Digite o código do cliente')
        self.cod.set_text('')

    #Botao localizar da tela pesquisa
    def botaLocalizarPesquisa(self,widget):
        codigo = self.cod.get_text()
        self.searchDadosCliente(codigo,widget=True)
        self.fecharTelaPesquisa(widget)

    #Pesquisa os dados de cliente
    def searchDadosCliente(self,codigo,widget):
        cliente = Conexao()
        self.mensagem.set_text(cliente.localizarDadosCliente(codigo))
        self.textNome.set_text(cliente.nome)
        self.textApelidio.set_text(cliente.apelidio)
        self.textEnd.set_text(cliente.logadouro)
        self.textNumero.set_text(str(cliente.numero))
        self.textBairro.set_text(cliente.bairro)
        self.textTelefone.set_text(cliente.telefone)

    #atualiza dados conforme o verificaodr de tela
    # 1 formulario de cliente
    # 2 formulario de carros
    # 3 formulario de manutencao
    def updateDados(self,widget):
        if self.verificadorTela ==1:
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
                self.limparTreeview(widget)
                self.carregaDadosTreview(widget)
            else:
                self.mensagem.set_text('Campo com (*) é obrigatório')

    #Deleta dados conforme veirificador de tela
    # 1 formulario de cliente
    # 2 formulario de carros
    # 3 formulario de manutencao
    def deleteDados(self,widget):
        if self.verificadorTela ==1:
            cliente = Conexao()
            codigo = self.cod.get_text()
            self.mensagem.set_text(cliente.deleteDadosCliente(codigo))
            self.limpaDadosClientes(widget)
            self.limparTreeview(widget)
            self.carregaDadosTreview(widget)

    #Limpa dados da tela
    def limpaDadosClientes(self,widget):
        self.textNome.set_text('')
        self.textApelidio.set_text('')
        self.textTelefone.set_text('')
        self.textEnd.set_text('')
        self.textNumero.set_text('')
        self.textBairro.set_text('')

    # Carrega os registros cadastrados
    def carregaDadosTreview(self,widget):
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

    #remove as colunas para nao duplicar as colunas
    def limparTreeview(self,widget):
        self.treeview.remove_column(self.column_text0)
        self.treeview.remove_column(self.column_text)
        self.treeview.remove_column(self.column_text1)
        self.treeview.remove_column(self.column_text2)
        self.treeview.remove_column(self.column_text3)
        self.treeview.remove_column(self.column_text4)
        self.treeview.remove_column(self.column_text5)

    # Mostra os botoe da horizontal
    def mostrarBtn(self,widget):
        self.btnSalvar.set_visible(True)
        self.btnEditar.set_visible(True)
        self.btnLocalizar.set_visible(True)
        self.btnExcluir.set_visible(True)
        self.btnCancelar.set_visible(True)

    #limpa tela home
    def limpaTelaHome(self,widget):
        self.logoPrincipal.clear()

    #Limpa toda a tela de cliente
    def limpaTelaCliente(self,widget):
        self.btnSalvar.set_visible(False)
        self.btnEditar.set_visible(False)
        self.btnLocalizar.set_visible(False)
        self.btnExcluir.set_visible(False)
        self.btnCancelar.set_visible(False)
        self.frameCliente.set_visible(False)
        self.gridCliente.set_visible(False)
        self.labelTitulo.set_text('')
        self.mensagem.set_text('')
        self.treeview.remove_column(self.column_text0)
        self.treeview.remove_column(self.column_text)
        self.treeview.remove_column(self.column_text1)
        self.treeview.remove_column(self.column_text2)
        self.treeview.remove_column(self.column_text3)
        self.treeview.remove_column(self.column_text4)
        self.treeview.remove_column(self.column_text5)

    #Fecha a tela de pesquisa
    def fecharTelaPesquisa(self,widget):
        self.telapesquisa.hide_on_delete()

    # Fecha o programa
    def sairTelaPrincipal(self, widget):
        Gtk.main_quit()

    def main(self):
        Gtk.main()

if __name__ == '__main__':
    aplicativo = Aplicativo()
    aplicativo.main()