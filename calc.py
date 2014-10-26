#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Calculatrice PyGtk
#  
#  Copyright 2014 Chiheb Nexus
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 3 of the License.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#  
################################################################################ 
############################ Main Gui ##########################################


from gi.repository import Gtk,GdkPixbuf
import os

class CalcApp(Gtk.Window):
    "Initialisation de la fenêtre principale"
    def __init__(self):
        Gtk.Window.__init__(self,title="Calculatrice PyGtk")
        self.set_icon_from_file("icon.png")
        
        self.set_default_size(250, 230)
        # Gui au centre de l'écran
        self.set_position(Gtk.WindowPosition.CENTER)
        # Menu : File/_Quitter + Aide/_Àpropos + Aide/_Plus
        action_group = Gtk.ActionGroup("Mes actions")
        self.add_fichier_menu_actions(action_group)
        self.add_aide_menu_actions(action_group)
        self.ui_file = os.getcwd() +"/gui_menu.xml"
        uimanager = self.create_ui_manager()
        uimanager.insert_action_group(action_group)
		
        menubar = uimanager.get_widget("/MenuBar")
        vbox = Gtk.VBox()
        # Liste des boutons 
        vbox.pack_start(menubar, False, False, 0)
        self.cls = Gtk.Button("Cls")
        self.cls.connect("clicked",self.calc,"Cls")
        self.bck = Gtk.Button("Bck")
        self.bck.connect("clicked",self.calc,"Bck")
        self.close = Gtk.Button("Close")
        self.close.connect("clicked",self.quitter)
        self.b0 = Gtk.Button("0")
        self.b0.connect("clicked",self.print_txt,"0")
        self.b1 = Gtk.Button("1")
        self.b1.connect("clicked",self.print_txt,"1")
        self.b2 = Gtk.Button("2")
        self.b2.connect("clicked",self.print_txt,"2")
        self.b3 = Gtk.Button("3")
        self.b3.connect("clicked",self.print_txt,"3")
        self.b4 = Gtk.Button("4")
        self.b4.connect("clicked",self.print_txt,"4")
        self.b5 = Gtk.Button("5")
        self.b5.connect("clicked",self.print_txt,"5")
        self.b6 = Gtk.Button("6")
        self.b6.connect("clicked",self.print_txt,"6")
        self.b7 = Gtk.Button("7")
        self.b7.connect("clicked",self.print_txt,"7")
        self.b8 = Gtk.Button("8")
        self.b8.connect("clicked",self.print_txt,"8")
        self.b9 = Gtk.Button("9")
        self.b9.connect("clicked",self.print_txt,"9")
        self.div = Gtk.Button("/")
        self.div.connect("clicked",self.calc,"/")
        self.fois = Gtk.Button("*")
        self.fois.connect("clicked",self.calc,"*")
        self.minus = Gtk.Button("-")
        self.minus.connect("clicked",self.calc,"-")
        self.plus = Gtk.Button("+")
        self.plus.connect("clicked",self.calc,"+")
        self.pt = Gtk.Button(".")
        self.pt.connect("clicked",self.print_txt,".")
        self.egal = Gtk.Button("=")
        self.egal.connect("clicked",self.calc,"=")
         
        # Créer un Table et placer les boutons
        table = Gtk.Table(5, 4, True)

        table.attach(self.cls, 0, 1, 0, 1)
        table.attach(self.bck, 1, 2, 0, 1)
        table.attach(Gtk.Label(), 2, 3, 0, 1)
        table.attach(self.close, 3, 4, 0, 1)

        table.attach(self.b7, 0, 1, 1, 2)
        table.attach(self.b8, 1, 2, 1, 2)
        table.attach(self.b9, 2, 3, 1, 2)
        table.attach(self.div, 3, 4, 1, 2)

        table.attach(self.b4, 0, 1, 2, 3)
        table.attach(self.b5, 1, 2, 2, 3)
        table.attach(self.b6, 2, 3, 2, 3)
        table.attach(self.fois, 3, 4, 2, 3)

        table.attach(self.b1, 0, 1, 3, 4)
        table.attach(self.b2, 1, 2, 3, 4)
        table.attach(self.b3, 2, 3, 3, 4)
        table.attach(self.minus, 3, 4, 3, 4)

        table.attach(self.b0, 0, 1, 4, 5)
        table.attach(self.pt, 1, 2, 4, 5)
        table.attach(self.egal, 2, 3, 4, 5)
        table.attach(self.plus, 3, 4, 4, 5)
        
        self.entree = Gtk.Entry()

        vbox.pack_start(self.entree, False, False, 0)
        vbox.pack_end(table, True, True, 0)

        self.add(vbox)

        self.connect("destroy", Gtk.main_quit)
        self.show_all()
        
    def print_txt (self,button,chiffre) :
        "Les numéros seront affichés dans la widget Entry"
        if chiffre == "." :
            chiffre = ','
        self.entree.insert_text(chiffre,position = 20)
        self.nombre = self.entree.get_text()
    
    def calc (self,widget,operator) :
        " Calculer les opérations"
        if operator == "Cls" :
            self.entree.set_text("")
        if operator == "Bck" :
            txt = self.entree.get_text()
            self.entree.set_text(txt[:len(txt)-1])
        elif operator == "+" :
            self.entree.set_text(self.nombre + "+")
        elif operator == "-" :
            b = self.entree.get_text()
            self.flag = 2
            self.entree.set_text(b+"-")
        elif operator == "*" :
            b = self.entree.get_text()
            self.entree.set_text(b+"*")
        elif operator == "/" :
            b = self.entree.get_text()
            self.entree.set_text(b+"/")
        elif operator == "=" :
            # Remplacer "," par "." pour faire les calculs
            # Et remplacer par "." par "," lors de l'affichage
            b = self.entree.get_text().replace(",",".")
            try :
                resultat = eval(b) # La magie de Python !!
                self.entree.set_text(str(resultat).replace(".",","))
            except :
                self.entree.set_text(b)
            
            
    def add_fichier_menu_actions(self,action_group) :
        """Ajouter le menu "Fichier"et ses sous-menus"""
        action_filemenu = Gtk.Action("FichierMenu","Fichier",None,None)
        action_group.add_action(action_filemenu)
        action_filequit = Gtk.Action("FichierQuitter","Quitter",None,None,Gtk.STOCK_QUIT)
        action_filequit.connect("activate",self.quitter)
        action_group.add_action(action_filequit)
				
    def add_aide_menu_actions (self,action_group) :
        """Ajouter le menu "Aide" et ses sous-menus  """
        action_aidemenu = Gtk.Action("AideMenu","Aide",None,None)
        action_group.add_action(action_aidemenu)
        action_aidepropos = Gtk.Action("AideApropos","À propos",None,None)
        action_aidepropos.connect("activate",self.propos)
        action_group.add_action(action_aidepropos)
        action_aideplus = Gtk.Action("AidePlus","Plus",None,None)
        action_aideplus.connect("activate",self.plus)
        action_group.add_action(action_aideplus)
        
    def quitter (self,widget) :
        " Pour quitter proprement"
        dialog = DialogQuit(self)
        response = dialog.run()
        if response == Gtk.ResponseType.OK :
            Gtk.main_quit()
        if response == Gtk.ResponseType.CANCEL :
            dialog.destroy()
            
    def propos (self,widget) : 
        "À propos"
        about = Gtk.AboutDialog()
        about.set_program_name("Calculatrice PyGtk")
        about.set_version("<b>Version :</b> 0.0.1")
        about.set_copyright("Chiheb NeXus© - 2014")
        about.set_comments("Calculatrice PygGtk est une calculatrice basique crée avec PyGtk3+ ")
        about.set_website("http://www.nexus-coding.blogspot.com")
        author = ["Chiheb Nexus http://www.nexus-coding.blogspot.com"]
        image = GdkPixbuf.Pixbuf.new_from_file("logo.png")
        about.set_icon_from_file("icon.png")
        about.set_logo(image)
        about.set_authors(author)
        about.set_license(" \
    Calculatrice PyGtk is a basic calculator based on PyGtk3+ \n \
    Copyright (C) 2014  Chiheb Nexus\n \
    This program is free software: you can redistribute it and/or modify \n\
    it under the terms of the GNU General Public License as published by\n\
    the Free Software Foundation, either version 3 of the License. \n \
    This program is distributed in the hope that it will be useful, \n\
    but WITHOUT ANY WARRANTY; without even the implied warranty of \n\
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.\n \
    See the GNU General Public License for more details. \n \
    You should have received a copy of the GNU General Public License \n\
    along with this program.  If not, see <http://www.gnu.org/licenses/>.")
		
        about.run()
        about.destroy()
        
    def plus(self,widget) : 
        "Pour plus d'informations"
        info = Gtk.MessageDialog(self,0,Gtk.MessageType.INFO,Gtk.ButtonsType.OK,\
                                        "Pour réporter un Bug ou pour plus d'informations :")
        info.format_secondary_text(" Veuillez visiter Github : https://github.com/Chiheb-Nexus/Calculatrice-PyGtk")
        info.run()
        info.destroy()
        
    def create_ui_manager (self) : 
        " Création de ui_manager "
        uimanager = Gtk.UIManager()
        uimanager.add_ui_from_file(self.ui_file) 
        return uimanager
        
class DialogQuit(Gtk.Dialog) :
    "Classe qui ouvre une fenêtre de dialog avant de quitter"
    def __init__(self,parent) : 
        Gtk.Dialog.__init__(self,"Quitter",parent,0,(Gtk.STOCK_CANCEL,Gtk.ResponseType.CANCEL,Gtk.STOCK_OK,Gtk.ResponseType.OK))
        self.set_default_size(150,100)
        label = Gtk.Label("Vous voulez vraiment quitter ?")
        box = self.get_content_area()
        box.add(label)
        self.show_all()
 
##### Test #####
if __name__ == '__main__' :
	win = CalcApp()
	Gtk.main()

