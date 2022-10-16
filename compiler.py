import os
import numpy as np


opcodes = {
	"NOP": 0x0,
	"ADD": 0x1,
	"SUB": 0x2,
	"AND": 0x3,
	"OR": 0x4,
	"JMP": 0x5,
	"JEQ": 0x6,
	"JNE": 0x7,
	"SD": 0x8,
	"LD": 0x9,
	"LI": 0xA,
	"MV": 0xB,
	"JAL": 0xC,
	"RET": 0xD,
	"JLT": 0xE,
	"JGT": 0xF
}

registers = {
	'A': 0,
	'B': 1,
	'C': 2,
	'D': 3
}

def transform(type, r1, r2, tag, counter, opcode):
	if type == "Operation":
		if registers.get(r1) == None:
			print(f"Register in line {counter} it's wrong: {r1}")
			return

		elif registers.get(r2) == None:
			print(f"Register in line {counter} it's wrong: {r2}")
			return

		r1 = registers.get(r1)
		r2 = registers.get(r2)
		
	elif type == "Data":
		if registers.get(r1) == None:
			print(f"Register in line {counter} it's wrong: {r1}")
			return

		elif registers.get(r2) == None:
			print(f"Register in line {counter} it's wrong: {r2}")
			return

		# tag = address[direccion]
	
	elif type == "Operation-Data":
		if registers.get(r1) == None:
			print(f"Register in line {counter} it's wrong: {r1}")
			return

		if tag > "4":
			pass
	
	n = (bin(opcode) + bin(r1) + bin(r2)).replace('0b', '')
	printed = int(n, 2)
	print(f"PC = {hex(counter)} (\n  Binary = {bin(printed).replace('0b', '')}\n  Hexadecimal = {hex(printed)}\n);")


def __main__():
	os.system("cls")
	file = input("Enter name's file: ")
	os.system("cls")

	try:
		asmcode = open(file, "r")
		

	except:
		print("No file found");
		os.system("pause")
		os.system("cls")
		exit(0)

	i = 0
	#code iterator
	while (True):
		linea = asmcode.readline()
		i += 1;
		linea = linea.split()

		if not linea:
			break
		
		opcode = opcodes.get(linea[0])
		print(f"{i}: {linea}")
		
		typeInst = -1
		reg1 = ""
		reg2 = ""
		tag = ""

		if opcode == 0:
			# binaryInst = "0x00"
			typeInst = -1
			reg1 = "A"
			reg2 = "B"

		elif opcode >= 1 and opcode <= 4:
			typeInst = "Operation"
			reg1 = linea[1].replace(',', '')
			reg2 = linea[2].replace(',', '')

		elif opcode == 10:
			typeInst = "Operation-Data"
			reg1 = linea[1].replace(',', '')
			tag = linea[2]

		elif opcode == None:
			print(f"Syntax error in line: {i} you put: {linea[0]}")
			exit(0)

		transform(typeInst, reg1, reg2, tag, i, opcode)	


	i = 0
	asmcode = open(file, "r")
	os.system("pause")
	os.system("cls")

__main__()