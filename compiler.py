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

def transform(type, r1, r2, counter):
	if type == 0:
		if registers.get(r1) == None:
			print(f"Register in line {counter} it's wrong: {r1}")
			return

		elif registers.get(r2) == None:
			print(f"Register in line {counter} it's wrong: {r2}")
			return

		r1 = registers.get(r1)
		r2 = registers.get(r2)
		
		
	if type == 1:
		pass


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
	
	typeInst = -1
	reg1 = ""
	reg2 = ""

	if opcode == 0:
		# binaryInst = "0x00"
		typeInst = -1
		reg1 = "A"
		reg2 = "B"

	elif opcode >= 1 and opcode <= 4:
		typeInst = 0
		reg1 = linea[1].replace(',', '')
		reg2 = linea[2].replace(',', '')

	elif opcode >= 5 and opcode <= 7:
		typeInst = 1

	elif opcode == None:
		print(f"Syntax error in line: {i} you put: {linea[0]}")
		exit(0)
	
	transform(typeInst, reg1, reg2, i)	

os.system("pause")
os.system("cls")

i = 0
asmcode = open(file, "r")
print("Codigo: ")

while (True):
	linea = asmcode.readline()

	if not linea:
		break
	print(f"{i}: {linea}")
	i += 1;
