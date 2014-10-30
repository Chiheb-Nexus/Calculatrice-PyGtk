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

from gi.repository import Gtk,Pango

class PyApp(Gtk.Window): 
    def __init__(self,widget):
        Gtk.Window.__init__(self,title="Choisir un font")
        self.set_resizable(False) # Fenêtre à taille fixe
        #self.set_size_request(350, 250)
        self.set_border_width(8)
        
        context = self.create_pango_context()
        self.fam = context.list_families()
        
        self.combo = Gtk.ComboBoxText() # Un ComboBoxText qui contient les fonts
        self.size = Gtk.ComboBoxText()  # UnComboBoxText qui contient les tailles
        label_font = Gtk.Label("Veuillez choisir un font")
        label_size = Gtk.Label("Veuillez choisir la taille")
        label_default = Gtk.Label("Font par défaut : Ubuntu  | Taille par défaut : 17")

        for ff in self.fam:
            self.combo.append_text(ff.get_name())  # Générer les fonts et les ajouter au ComboBoxText
        for ss in range(31) :
            self.size.append_text(str(ss))  # Générer les tailles de 1 à 30 et les ajouter au ComboBoxText
        
        button = Gtk.Button("Valider")
        button2 = Gtk.Button("Annuler")
        button2.connect("clicked",self.annuler)
        button.connect("clicked",self.get_status)
        
        vbox = Gtk.VBox()
        hbox = Gtk.HBox()
        
        vbox.pack_start(label_font,False,False,0)
        vbox.pack_start(self.combo,False,False,0)
        vbox.pack_start(label_size,False,False,0)
        vbox.pack_start(self.size,False,False,0)
        vbox.pack_start(label_default,False,False,0)
        hbox.pack_start(button2,True,True,0)
        hbox.pack_start(button,True,True,0)
        vbox.pack_end(hbox,True,False,0)

        self.add(vbox)
        
        self.set_position(Gtk.WindowPosition.CENTER)
        self.show_all()
        
    def get_status(self,widget) :
        "Font et taille choisies"
        #PyApp.font et PyApp.taille deux variables
        # qui peuvent être utilisés par les autres classes
        PyApp.font = self.combo.get_active_text() 
        PyApp.taille = self.size.get_active_text()
        self.destroy() # Détruire la fenêtre
        
    def annuler(self,widget) :
        "Annuler la saisie du font et de la taille"
        
        self.destroy()



    

