import firebase_admin
from firebase_admin import db

#Anexo a la base de datos, conexion a la misma
cred_obj = firebase_admin.credentials.Certificate('C:\\Users\\Camila\\Documents\\P.O.O\\BaseDatoTrabajoFinal\\bd-usuarios-y-mascotas-firebase-adminsdk-x91j7-4e095bd271.json')
databaseURL = 'https://bd-usuarios-y-mascotas-default-rtdb.firebaseio.com/'
default_app = firebase_admin.initialize_app(cred_obj, {
	'databaseURL':databaseURL
	})

ref = db.reference("/") #Me estoy parando en el inicio de mi base de datos

