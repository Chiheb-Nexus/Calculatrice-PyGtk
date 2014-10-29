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

from gi.repository import Gtk,GdkPixbuf

class DialogQuit(Gtk.Dialog) :
    "Classe qui ouvre une fenêtre de dialog avant de quitter"
    def __init__(self,parent) : 
        Gtk.Dialog.__init__(self,"Quitter",parent,0,(Gtk.STOCK_CANCEL,Gtk.ResponseType.CANCEL,Gtk.STOCK_OK,Gtk.ResponseType.OK))
        self.set_default_size(150,100)
        label = Gtk.Label("Vous voulez vraiment quitter ?")
        box = self.get_content_area()
        box.add(label)
        self.show_all()

class MenuAnnex() :
	def __init__(self) :
		"Classe qui contien les méthodes de la class CalcApp"


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
		action_aidepropos.connect("activate",MenuAnnex.propos,"a")
		action_group.add_action(action_aidepropos)
		action_aideplus = Gtk.Action("AidePlus","Plus",None,None)
		action_aideplus.connect("activate",self.plus)
		action_group.add_action(action_aideplus)

	def create_ui_manager (self) : 
		" Création de ui_manager "
		uimanager = Gtk.UIManager()
		uimanager.add_ui_from_file(self.ui_file) 
		return uimanager

	

	def propos (self,widget) :
		"À propos"
		about = Gtk.AboutDialog()
		about.set_program_name("Calculatrice PyGtk")
		about.set_version("<b>Version :</b> 0.0.3")
		about.set_copyright("Chiheb NeXus© - 2014")
		about.set_comments("Calculatrice PygGtk est une calculatrice basique crée avec PyGtk3+ ")
		about.set_website("http://www.nexus-coding.blogspot.com")
		author = ["Chiheb Nexus http://www.nexus-coding.blogspot.com"]
		image = GdkPixbuf.Pixbuf.new_from_file("images/logo.png")
		about.set_icon_from_file("images/icon.png")
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


	