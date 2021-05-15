import configparser,os.path
from O365 import Account
from datetime import datetime, timedelta
from O365.excel import WorkBook

ruta = os.getcwd()
try:
   print("Ejecutando en {}".format(ruta))
   #cargar configuración inicial
   config = configparser.ConfigParser()
   config.read(ruta+'\\initParams.txt')
   app_id = config.get('O365','app_id')
   app_sc = config.get('O365','app_sc')
   #definir credenciales
   credentials = (app_id, app_sc)
   account = Account(credentials)
   #validar token
   if not account.is_authenticated:
      print("Usuario NO autenticado! Continuar en la consola de Python para obtener un token válido")
      #solicitar nuevo inicio de sesión
      if account.authenticate(scopes=['basic','onedrive']):
         cu = account.get_current_user()
         print("Autenticación correcta con usuario: {}".format(cu.mail))
   else:
      cu = account.get_current_user()
      print("Autenticado con usuario: {}".format(cu.mail))
      storage = account.storage()
      my_drive = storage.get_default_drive()
      shared_folder = my_drive.get_shared_with_me()
      for item in shared_folder:
         print(item)
         if item.name == "prueba.xlsx":
            #item.download(to_path='E:\Documentos\Calidda\Reporte Directorio')
            print("encontrado!")
            #excel_file = WorkBook(item,use_session=False, persist=False)
            #ws = excel_file.get_worksheet('Hoja1')
            #celda = ws.get_range('C1')
            #print("valor: " + celda.values[0][0])
            #onedrive_file = my_drive.get_item(item.object_id)
         if item.name == "OPEX 2021":
            for f in item.get_items():
               print("{} > {}".format(item.name,f.name))
               if f.name == "OPEX 2021.xlsx":
                  excel_file = WorkBook(f,use_session=False, persist=False)
                  ws = excel_file.get_worksheet('OPEX 2021 (4)')
                  celda = ws.get_range('J8')
                  print("valor: " + str(celda.values[0][0]))

except Exception as ex:
   errmsj = "-".join(ex.args)
   print(errmsj)
print("Fin de proceso")
