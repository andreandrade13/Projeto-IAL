#!/usr/bin/python3
#_*_coding:UTF-8-*-
	# criação e inserção de dados no arquivo binário

import struct
i=1
arquivo=open('arq_func.dat','wb')
while True:
	print('\n%/do. funcionario: \n' % i)
	codigo=int(input('Codigo-funcionario:'))
	if codigo==9999: break
	nome=input('Nome-funcionario',[30])
	salario=float(input('salario')
	registro=struct.pack('i30sf',codigo,nome.encode('ascii'),salario)
	arquivo.write(registro)
	i+=1
arquivo.close
