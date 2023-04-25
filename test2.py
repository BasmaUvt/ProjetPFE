#import win32com.client
#outlook = win32com.client.Dispatch("Outlook.Application")
#mapi = outlook.GetNamespace("MAPI")
#test_folder = mapi.Folders("test")
#test_folder = mapi.GetDefaultFolder(6).Folders("test") # Assuming "test" is a subfolder of the Inbox

#count = 0
#for item in test_folder.Items:
 #   if item.Attachments.Count > 0:
#        count += item.Attachments.Count

#print(f"Number of attachments in the 'test' folder: {count}")

import win32com.client
#mapi = win32com.client.Dispatch("Outlook.Application").GetNamespace("MAPI")
#mapi.GetNamespace("MAPI").Logon(None, None, MAPI_DEFERRED_ERRORS)
import pandas as pd
import openpyxl
from openpyxl.styles import (PatternFill, colors)
from openpyxl import Workbook
import os
import os.path

from datetime import datetime
from time import sleep
import time
outlook = win32com.client.Dispatch("Outlook.Application")
mapi = outlook.GetNamespace("MAPI")

# Récupérer la boîte de réception
inbox = mapi.GetDefaultFolder(6)

# Récupérer la liste des noms de tous les dossiers dans la boîte de réception
folders = [folder.Name for folder in inbox.Folders]

# Afficher la liste des noms des dossiers
print(folders)

def count_attachments(folder):
    count = 0
    for item in folder.Items:
        for attachment in item.Attachments:
            count += 1
    return count

test_folder = mapi.GetDefaultFolder(6).Folders("ch")
print(f"Nombre de pièces jointes dans le dossier 'ch': {count_attachments(test_folder)}")

count_emails = len(test_folder.Items)
print(f"Nombre d'emails dans le dossier 'ch': {count_emails}")
# Vérifier si le dossier "test" est présent
#if "ch" in folders:
#    test_folder = inbox.Folders("ch")
#    print(f"Nombre de pièces jointes dans le dossier 'ch': {count_attachments(test_folder)}")
#else:
#    print("Le dossier 'ch' n'existe pas dans la boîte de réception.")


