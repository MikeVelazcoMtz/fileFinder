#!/usr/bin/env python
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

def validate( message, isRoute = False ):
	data = str( raw_input(message) )
	errorMessage = "Error. " + message
	while True:
		if data == "":
			data = str( raw_input( errorMessage ) )				
		else:
			if isRoute:
				try:
					dirList = os.listdir( data )
					break
					break
				except Exception, e:
					data = ""
			else:
				break
	
	return data

print "Bienvenido a FileFinder"
print "Miguel Angel Velazco 2014"

path          = validate("Ingrese La ruta ABSOLUTA para la busqueda: ", True)
search        = validate("Ingrese los datos que desee buscar: ")
searchType 	  = validate("""Ingrese El tipo de busqueda:
	    # -f  : para buscar un archivo/directorio con tal nombre
	    # -s  : para buscar dentro de los arhivos
	    # N/n : para ejecutar la busqueda inmediatamente. """)
fileExtension = validate("Ingrese el nombre de la extension del archivo que desee buscar: ")

findFile(path, search, searchType, fileExtension)