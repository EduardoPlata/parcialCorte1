from config.db import BASE


def ingresoValidar(info):
                
    dato =""
    bandera = 1
                
    while bandera!=0:
        dato = input('Ingrese '+info+': ')
        if not dato:
            print("Porfavor ingrese")        
        else:
            print("Se registro "+info)
            return dato

#_______________________________________________________
def crearUsuario(usuario):
    #print(usuario)
    #dato = ['mama','meme','mimi']
    cursor=BASE.cursor()
    cursor.execute('''
        insert into usuarios(nombre,email,contrasena)
        values (%s,%s,%s)''',
        (usuario['nombre'],
        usuario['email'],
        usuario['contrasena']))
    ''' cursor.execute('        insert into usuarios(nombre,email,contrasena)        values (%s,%s,%s)',        (dato)) '''
    BASE.commit()
    cursor.close()

def crear():
    newUser ={
        'nombre' : ingresoValidar('nombre'),
        'email' : ingresoValidar('email'),
        'contrasena' : ingresoValidar('contrasena')
    }
    crearUsuario(newUser)