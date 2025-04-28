import shutil
import os
import time
from datetime import datetime
from googleapiclient.discovery import build
from google.oauth2 import service_account
from googleapiclient.http import MediaFileUpload, MediaIoBaseDownload
import io
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request


cartella_download = 'C:\\Users\\Gabin\\Desktop\\python\\cartellaA\\'


json_key = 'C:\\Users\\Gabin\\Desktop\\python\\pythonapimaps-430414-0007a25f.json'
#global folder_drive
folder_drive = '1JCjOHAkrBeXsJFQmvlXKvoUFZ3pz'


def authenticate_with_service_account():
    creds = service_account.Credentials.from_service_account_file(json_key, scopes=['https://www.googleapis.com/auth/drive','https://www.googleapis.com/auth/drive.file','https://www.googleapis.com/auth/drive.metadata'])
    drive_service = build('drive', 'v3', credentials=creds)
    return drive_service



def set_viewer_permission(file_id):
    drive_service = authenticate_with_service_account()
    new_permission = {
    'type': 'anyone',
    'role': 'reader'
    }

    folder = drive_service.permissions().create(fileId=file_id,body=new_permission).execute()

    print(f"Access change as 'Viewer' for the file ID: {file_id}")



def set_editor_permission(file_id):
    drive_service = authenticate_with_service_account()
    new_permission = {
    'type': 'anyone',
    'role': 'writer'
    }

    folder = drive_service.permissions().create(fileId=file_id,body=new_permission).execute()

    print(f"Access change as 'Editor' for the file ID: {file_id}")



def upload_file(file_name, parent_id):
    try:
        drive_service = authenticate_with_service_account()
        
        file_metadata = {
            'name': file_name,  
            'parents': [parent_id]  # ID of the folder where you want to upload
        }
        file_path = file_name

        media = MediaFileUpload(file_path, resumable=True)

        file = drive_service.files().create(body=file_metadata, media_body=media, fields='id').execute()
        return file.get('id')

        answer = int(input("you want to set your file like viewer o editor:    0.viewer     1.editor: "))
        if answer == 0:
            set_viewer_permission(file.get('id'))

        elif answer == 1:
            set_editor_permission(file.get('id'))

        else:
            print("your file would be set in the default form")
            
    except Exception as error_message:
        print(error_message)



def folder_in_drive(folder_name, parent_id):
    drive_service = authenticate_with_service_account()
    
    folder_metadata = {
    'name': folder_name,
    'mimeType': 'application/vnd.google-apps.folder',
    'parents':[parent_id] # ID of the parent folder (optional)
    }

    folder = drive_service.files().create(body=folder_metadata, fields='id', supportsAllDrives=True).execute()
    return folder.get('id')


# UPLOAD di una CARTELLA dal PC su Google Drive
def upload_folder_to_drive(folder_path, parent_id):
    service = authenticate_with_service_account() # Autenticazione e ottenimento del servizio Google Drive
    #folder_name = os.path.basename(folder_path)
    #folder_id = creaCARTELLA(folder_name, parent_id) #su Drive crea la cartella 'A' (con lo stesso nome di quella di PARTENZA da fare il BACKUP)
    dizionarioIDsuDRIVE={}
    penultimonamediROOT=''
    count = 0
    for root, dirs, files in os.walk(folder_path): ## cicla tante volte =pari al NUMERO di TUTTE le cartelle+sottocartelle che trova nell'ALBERO di scansione (aggiungi anche quella di PARTENZA)
        print("\nROOT",root) #ciclo1 'A' , ciclo2 'A/test' , ciclo3 'A/test/boo', ciclo4 'A/test/boo/casino1', ciclo5 'A/test/boo/casino2', ciclo6 'A/test/teeest'
        #print("DIR", dirs)
        #print("FILES", files) 
        print(f"-- UPLOAD in corso di {len(files)} file...")

        
        ### PASSO 1) mi serve l'ID PADRE (è il penultimo nome di Cartella) preso dalla ROOT
        #ESTRAGGO il penultimonome dalla ROOT. 1°giro: ROOT='A' ho '' 2°giro: ROOT='A/test' ho 'test' 3°giro: ROOT='A/test/boo' ho 'boo'
        listanomiCartelle = root.split(os.sep)[:-1]# LISTA dei nomidiCartelle che formano la ROOT ['A', 'test', 'boo'] #root.rsplit("\\")[-2]
        if listanomiCartelle!=[]: #al primo ciclo ho ROOT='A' ma crea la listanomiCArtelle=[] VUOTA!
            penultimonamediROOT=listanomiCartelle[-1] #se ROOT='A/test/boo/casino1' estraggo 'boo'
            #parent_id=dizionarioIDsuDRIVE[penultimonamediROOT]
            print(penultimonamediROOT) #PENULTIMO nome che serve per estrarre l'ID PADRE per poi creare la cartella FIGLIO
        count += 1  
        #LEGGO dal dizionario 'dizionarioIDsuDRIVE' l'ID conoscendo il 'penultimonamediROOT'
        if penultimonamediROOT!='' and count > 1 :
            parent_id=dizionarioIDsuDRIVE[penultimonamediROOT]
            print(parent_id)

            
        ### PASSO 2) sapendo l'ID della cartella precedente (PADRE) posso creare la CARTELLA FIGLIO
        #CREA la CARTELLA su Drive col nome
        folder_name = os.path.basename(root) #estra l'ultima parola della ROOT 'A/test/teeest' prende 'teeest'
        print(folder_name)
        folder_id = folder_in_drive(folder_name, parent_id) #su Drive crea la cartella 'A' (con lo stesso nome di quella di PARTENZA da fare il BACKUP)
        dizionarioIDsuDRIVE[folder_name]=folder_id # {'A': '1s23d45gfby6'}
        print(dizionarioIDsuDRIVE)

        ### PASSO 3) fare l'UPLOAD dei file nella cartella FIGLIO appena creata
        for namef in files:
            #print("\n",namef)
            pathf= os.path.join(root, namef) # 'A\file1.txt' 'A\test\file2.pdf'
            upload_file(pathf,folder_id) # carica i FILE della ROOT corrente da PC su Drive (nella cartella FIGLIO)



upload_folder_to_drive('C:\\Users\\Gabin\\Desktop\\python\\cartellaA', folder_drive)






def file_name_ids_in_folder(folder):
    try:
        query = f"'{folder}' in parents"
        drive_service = authenticate_with_service_account() 
        results = drive_service.files().list(q=query, fields='files(id, name,mineType)').execute()
        items = results.get('files', [])

        if not items:
            print('the folder is empty')
        else:
            print('file/folder find in the folder:')
            for item in items:
                print(f"Nome: {item['name']}, ID: {item['id']}")

        return items

    except HttpError as error:
        print(f"An error occurred: {error}")
        return None




def download_from_drive(folder):
    drive_service = authenticate_with_service_account()
    info = file_name_ids_in_folder(folder)
    for inf in info:
        file_id = inf['id']
        file_path = cartella_download+inf['name']
        if inf['mineType'] == 'application/vnd.google-apps.folder':
            new_folder_path = os.path.join(cartella_download+inf['name'], inf['name'])
            if not os.path.exists(cartella_download):
                os.makedirs(cartella_download)

        request = drive_service.files().get_media(fileId=file_id)
        fh = io.FileIO(file_path, mode='wb')
        downloader = MediaIoBaseDownload(fh, request)
        done = False

    while not done:
        status, done = downloader.next_chunk()
        print("Download %d%%." % int(status.progress() * 100))


