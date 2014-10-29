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
from methodes import *
import re
import os
from math import sqrt,tan,sin,cos,log2,log10,pi,factorial
class CalcApp(Gtk.Window):
    "Initialisation de la fenêtre principale"
    def __init__(self):
        Gtk.Window.__init__(self,title="Calculatrice PyGtk")
        self.set_icon_from_file("images/icon.png")
        self.set_resizable(False)  # Fenêtre de taille fixe
        #self.set_default_size(250,200)
        # Gui au centre de l'écran
        self.set_position(Gtk.WindowPosition.CENTER)

        # Menu : File/_Quitter + Aide/_Àpropos + Aide/_Plus
        action_group = Gtk.ActionGroup("Mes actions")
        MenuAnnex.add_fichier_menu_actions(self,action_group)
        MenuAnnex.add_aide_menu_actions(self,action_group)
        self.ui_file = os.getcwd() +"/gui_menu.xml"
        uimanager = MenuAnnex.create_ui_manager(self)
        uimanager.insert_action_group(action_group)

        menubar = uimanager.get_widget("/MenuBar")
        vbox = Gtk.VBox()

        # Liste des boutons 
        vbox.pack_start(menubar, False, False, 0)

        # Ajouter une image au bouton de Clear Screen
        image = Gtk.Image()
        image.set_from_stock(Gtk.STOCK_REFRESH,3)
        self.cls = Gtk.Button()
        self.cls.set_image(image)
        self.cls.connect("clicked",self.calc,"Cls")
        
        image = Gtk.Image()
        image.set_from_stock(Gtk.STOCK_CLEAR,3)
        self.bck = Gtk.Button()
        self.bck.set_image(image)
        self.bck.connect("clicked",self.calc,"Bck")

        # Ajouter une image au bouton Close
        image2 = Gtk.Image()
        image2.set_from_stock(Gtk.STOCK_CLOSE,3)
        self.close = Gtk.Button()
        self.close.set_image(image2)
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
        self.div = Gtk.Button("÷")
        self.div.connect("clicked",self.calc,"/")
        self.fois = Gtk.Button("×")
        self.fois.connect("clicked",self.calc,"*")
        self.minus = Gtk.Button("-")
        self.minus.connect("clicked",self.calc,"-")
        self.plus = Gtk.Button("+")
        self.plus.connect("clicked",self.calc,"+")
        self.pt = Gtk.Button(",")
        self.pt.connect("clicked",self.print_txt,",")
        self.egal = Gtk.Button("=")
        self.egal.connect("clicked",self.calc,"=")
        self.p1 = Gtk.Button("(")
        self.p1.connect("clicked",self.print_txt,"(")
        self.p2 = Gtk.Button(")")
        self.p2.connect("clicked",self.print_txt,")")
        self.racine = Gtk.Button("√")
        self.racine.connect("clicked",self.print_txt,"√")
        self.cos = Gtk.Button("cos")
        self.cos.connect("clicked",self.print_txt,"cos")
        self.sin = Gtk.Button("sin")
        self.sin.connect("clicked",self.print_txt,"sin")
        self.tan = Gtk.Button("tan")
        self.tan.connect("clicked",self.print_txt,"tan")
        self.ln = Gtk.Button("Ln")
        self.ln.connect("clicked",self.print_txt,"ln")
        self.log = Gtk.Button("Log")
        self.log.connect("clicked",self.print_txt,"log")
        self.xy = Gtk.Button("x^y")
        self.xy.connect("clicked",self.print_txt,'^')
        self.pii = Gtk.Button("π")
        self.pii.connect("clicked",self.print_txt,"π")
        self.fac = Gtk.Button("!")
        self.fac.connect("clicked",self.print_txt,"!")

         
        # Créer un Table et placer les boutons
        table = Gtk.Table(5, 7, True)

        table.attach(self.cls, 0, 1, 0, 1)
        table.attach(self.bck, 1, 2, 0, 1)
        table.attach(Gtk.Label(), 2, 3, 0, 1)
        table.attach(self.close,6,7,0,1)

        table.attach(self.b7, 0, 1, 1, 2)
        table.attach(self.b8, 1, 2, 1, 2)
        table.attach(self.b9, 2, 3, 1, 2)
        table.attach(self.p1, 3, 4, 1, 2)
        table.attach(self.p2,4,5,1,2)
        table.attach(self.pii,5,6,1,2)
        table.attach(self.xy,6,7,1,2)

        table.attach(self.b4, 0, 1, 2, 3)
        table.attach(self.b5, 1, 2, 2, 3)
        table.attach(self.b6, 2, 3, 2, 3)
        table.attach(self.fois, 3, 4, 2, 3)
        table.attach(self.div,4,5,2,3)
        table.attach(self.cos,5,6,2,3)
        table.attach(self.sin,6,7,2,3)

        table.attach(self.b1, 0, 1, 3, 4)
        table.attach(self.b2, 1, 2, 3, 4)
        table.attach(self.b3, 2, 3, 3, 4)
        table.attach(self.minus, 3, 4, 3, 4)
        table.attach(self.plus,4,5,3,4)
        table.attach(self.tan,5,6,3,4)
        table.attach(self.ln,6,7,3,4)

        table.attach(self.b0, 0, 1, 4, 5)
        table.attach(self.pt, 1, 2, 4, 5)
        table.attach(self.egal, 2, 4, 4, 5)
        table.attach(self.racine, 4, 5, 4, 5)
        table.attach(self.log,5,6,4,5)
        table.attach(self.fac,6,7,4,5)
        self.entree = Gtk.Entry()
        

        vbox.pack_start(self.entree, True, True, 10)
        vbox.pack_end(table, True, True, 0)

        self.add(vbox)

        self.connect("destroy", Gtk.main_quit)
        self.show_all()
        
    def print_txt (self,button,chiffre) :
        "Les numéros seront affichés dans la widget Entry"
        self.entree.insert_text(chiffre,position = 40)
        self.nombre = self.entree.get_text()
    
    def calc (self,widget,operator) :
        " Calculer les opérations"
        if operator == "Cls" :
            self.entree.set_text("")
        if operator == "Bck" :
            txt = self.entree.get_text()
            self.entree.set_text(txt[:len(txt)-1])
        elif operator == "+" :
            b = self.entree.get_text()
            self.entree.set_text(b + "+")
        elif operator == "-" :
            b = self.entree.get_text()
            self.entree.set_text(b+"-")
        elif operator == "*" :
            b = self.entree.get_text()
            self.entree.set_text(b+"×")
        elif operator == "/" :
            b = self.entree.get_text()
            self.entree.set_text(b+"÷")
        elif operator == "=" :
            # Remplacer "," par "." pour faire les calculs
            # Et remplacer "." et "/" par "," et "÷" lors de l'affichage
            b1 = self.entree.get_text()
            b = self.calcul_avance(b1)
            
            try :
                resultat = str(eval(b.replace("ln","log2"))) # La magie de Python !!
                self.entree.set_text(self.affichage_avancee(resultat))
            except :
                self.entree.set_text(b1)
                
    def calcul_avance (self,a) :
        "Modification de la Gtk.Entry pour la calculer"
        a = a.replace(",",".")
        a = a.replace("÷","/")
        a = a.replace("×","*")
        a = re.sub(r'√(\d*\.?\d+)', r'√(\1)', a).replace("√","sqrt")
        a = re.sub(r'cos(\d*\.?\d+)', r'cos(\1)', a)
        a = re.sub(r'sin(\d*\.?\d+)', r'sin(\1)', a)
        a = re.sub(r'tan(\d*\.?\d+)', r'tan(\1)', a)
        a = re.sub(r'ln(\d*\.?\d+)', r'ln(\1)', a)
        a = re.sub(r'log(\d*\.?\d+)', r'log(\1)', a).replace("log","log10")
        a = re.sub(r'π(\d*\.?\d+)', r'π(\1)', a).replace("π","pi")
        a = a.replace("^","**")
        a = re.sub(r'!(\d*\.?\d+)', r'!(\1)', a).replace("!","factorial")

        # Remerciements à arshajii du forum stackoverflow.com 
        return a

    def affichage_avancee (self,a) :
        "Affichage avancé"
        a = a.replace("/","÷")
        a = a.replace(".",",")
        

        return a

    def quitter (self,widget) :
        " Pour quitter proprement"
        dialog = DialogQuit(self)
        response = dialog.run()
        if response == Gtk.ResponseType.OK :
            Gtk.main_quit()
        if response == Gtk.ResponseType.CANCEL :
            dialog.destroy()

    def plus(self,widget) : 
        "Pour plus d'informations"
        info = Gtk.MessageDialog(self,0,Gtk.MessageType.INFO,Gtk.ButtonsType.OK,"Pour réporter un Bug ou pour plus d'informations :")
        info.format_secondary_text(" Veuillez visiter Github : https://github.com/Chiheb-Nexus/Calculatrice-PyGtk")
        info.run()
        info.destroy()

            
   
        

 
##### Test #####

if __name__ == '__main__' :
	win = CalcApp()
	Gtk.main()

