nombre = "Juan"  ##variables de tipo string
apellido = "Pérez"

print (nombre)
print (apellido)       ##variables de diferente tipo y las une con print 
print (nombre + " " + apellido)

numero = 10
numero = 100       ##variables enteras 
print (numero)

numero = 10
numero *= 100   ##variables que se multiplican entre si
print (numero)

numero = 10
numero -= 100   ## variables que se restan entre si
print (numero)

numero = 10
numero += 100  ##variables que se suman entre si
print (numero)

nombre = " Juan "
bienvenido = "hola," + nombre + "¿como esta?"    ##concatenacion de variables
print (bienvenido)

nombre = " 600 "
bienvenido = f"hola {nombre} ¿como esta?"   ##concatenacion de variables con f-string {}
print (bienvenido)

nombre = " 600 "  ##del
bienvenido = f"hola {nombre} ¿como esta?"
del bienvenido ## elimina la variable bienvenido
print (bienvenido)

nombre = " 600 "
del nombre ## si la elimina porque esta antes de haberla declarado con {}
bienvenido = f"hola {nombre} ¿como esta?"
print (bienvenido)
