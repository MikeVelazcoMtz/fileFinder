from fnmatch import fnmatch
import os,sys

def findFile( path, search, searchType, fileExtension ):
	try:
		dirList = os.listdir( path )
	except OSError:
		print "Ha sucedido un error. Revise su ruta"
	else:
		for l in dirList:
			route = path + "/" + l
			if os.path.isfile( route ) == True:#archivo
				if searchType == "-s" and ( fileExtension == "" or fnmatch( l, "*." + fileExtension ) ): # Buscado por extension
						File = open( route )
						i = 1
						while True:
							line = File.readline()
							if not line:
								break
							else:
								if line.find( search ) > 0:
									print "Cadena encontrada en el archivo: " + route + " .LINEA " + str( i )
							i += 1
						#print str(i)
				else:# Buscando por nombre de archivo/Carpeta
					if l.find( search ) > 0:
						print "Archivo Encontrado: " + route
				#print path + "/" + l
			else:#directorio
				if ( l.find( search ) > 0 or l.startswith(search) ) and searchType == "-f":
					print "Directorio Encontrado " + route
				findFile( route, search, searchType, fileExtension )

try:
	filePath = sys.argv[ 1 ]
	searchString = sys.argv[ 2 ]
	searchType = sys.argv[ 3 ]
	if len( sys.argv ) > 4:
		fileExtension = sys.argv[ 4 ]
	else:
		fileExtension = ""
	
	if fileExtension != "":	
		print "(" + fileExtension+ ")"
except IndexError:
	print """Error.Hacen falta argumentos. 
		Sintaxis: python fileFinder.py [ruta] [busqueda] [ -s{cadena en archivo},-f{Nombre de archivo} ] [extension del archivo]"""
else:
	routeDefiner = filePath[ 0 ]
	if routeDefiner == "/":
		#print "La busqueda inicia desde el directorio Raiz!!"
		if searchType == "-s" or searchType == "-f":
			findFile(filePath, searchString, searchType, fileExtension)
		else:
			print """Error. Debe asignar el tipo de busqueda:
				- Para buscar un archivo por su nombre utilice -f
				- Para buscar una cadena dentro de los archivos en la ruta utilice -s"""
	else:
		#print "La busqueda inicia desde la direccion del archivo :D"
		absDir = os.path.abspath(__file__)
		dirList = os.listdir( absDir.replace("fileFinder.py","") )
		if searchType == "-s" or searchType == "-f":
			findFile(filePath, searchString, searchType, fileExtension)
		else:
			print """Error. Debe asignar el tipo de busqueda:
				- Para buscar un archivo por su nombre utilice -f
				- Para buscar una cadena dentro de los archivos en la ruta utilice -s"""