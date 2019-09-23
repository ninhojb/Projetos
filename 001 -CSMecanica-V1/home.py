import gi
gi.require_version('Gtk','3.0')
from gi.repository import Gtk


class Home:

    def __init__(self):
        # atribui o grid fixo home e logo
        self.builder = Gtk.Builder()
        self.logoPrincipal = self.builder.get_object('img_logo')
        self.fixo_home = self.builder.get_object('fixo_home')
        self.imgLogo = 'img/logo.jpg'
        self.logoPrincipal.set_from_file(self.imgLogo)
        self.logoPrincipal.show()
        self.fixo_home.set_visible(True)
