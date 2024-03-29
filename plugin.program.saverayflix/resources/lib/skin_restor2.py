#!/usr/bin/python3
# creation par rayflix le 23 10 21
import xbmc
from io import BytesIO
from urllib.request import urlopen
from zipfile import ZipFile
import shutil
import sys

# copie des fichiers sauvegarde
source_dir = xbmc.translatePath('special://home/userdata/addon_data/Scripts/Skin_save/2/addon_data')
destination_dir = xbmc.translatePath('special://home/userdata/addon_data')
source_dir2 = xbmc.translatePath('special://home/userdata/addon_data/Scripts/Skin_save/2/addons/skin.project.aura')
destination_dir2 = xbmc.translatePath('special://home/addons/skin.project.aura')
shutil.copytree(source_dir, destination_dir, dirs_exist_ok=True)
shutil.copytree(source_dir2, destination_dir2, dirs_exist_ok=True)

xbmc.executebuiltin("Notification(COPIE OK,Mise à jour effectuée !)")
xbmc.sleep(5000)

# actualisation du skin
xbmc.executebuiltin("Notification(ACTUALISATION DU SKIN, Skin Save 2...)")
xbmc.sleep(2000)
xbmc.executebuiltin('ReloadSkin')

sys.exit()