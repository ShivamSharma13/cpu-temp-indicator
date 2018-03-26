import gi
import os
gi.require_version('Gtk' , '3.0')
gi.require_version('AppIndicator3', '0.1')

from gi.repository import Gtk as gtk 
from gi.repository import AppIndicator3 as appindicator 

import signal

signal.signal(signal.SIGINT, signal.SIG_DFL)
APPINDICATOR_ID = 'myappindicator'

def main():
	indicator = appindicator.Indicator.new(APPINDICATOR_ID, os.path.abspath('icon.svg') , appindicator.IndicatorCategory.SYSTEM_SERVICES)
	indicator.set_status(appindicator.IndicatorStatus.ACTIVE)
	indicator.set_menu(build_menu(indicator))
	gtk.main()


def build_menu(indicator):
    menu = gtk.Menu()
    item_quit = gtk.MenuItem('Quit')
    item_quit.connect('activate', quit)
    item_change_icon = gtk.MenuItem('Change')
    item_change_icon.connect('activate' , change , indicator)
    menu.append(item_change_icon)
    menu.append(item_quit)
    menu.show_all()
    return menu
 

def quit(source):
    gtk.main_quit()


def change(source , indicator):
	indicator.set_icon(os.path.abspath('icon1.svg'))
	indicator.set_label("hello" , "hello")


if __name__ == "__main__":
	main()