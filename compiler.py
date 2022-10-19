import os
import numpy as np


opcodes = {
	"NOP": 0,
	"ADD": 1,
	"SUB": 2,
	"AND": 3,
	"OR": 4,
	"JMP": 5,
	"JEQ": 6,
	"JNE": 7,
	"SD": 8,
	"LD": 9,
	"LI": 10,
	"MV": 11,
	"JAL": 12,
	"RET": 13,
	"JLT": 14,
	"JGT": 15
}

registers = {
	'A': 0,
	'B': 1,
	'C': 2,
	'D': 3,
	'$0': 0,
	'$1': 1,
	'$2': 2,
	'$3': 3
}


def transform(type, r1, r2, imm, counter, opcode):
	if type == "Operation":
		if registers.get(r1) == None:
			print(f"Register in line {counter} it's wrong: {r1}")
			return

		elif registers.get(r2) == None:
			print(f"Register in line {counter} it's wrong: {r2}")
			return

		r1 = registers.get(r1)
		r2 = registers.get(r2)

		# print
		opcode = bin(opcode).replace('0b', '')
		opcode = opcode.zfill(4)

		r1 = bin(r1).replace('0b', '')
		r1 = r1.zfill(2)
		r2 = bin(r2).replace('0b', '')
		r2 = r2.zfill(2)
		printed = (opcode + " " + r1 + r2)
		hexPrinted = hex(int(opcode + r1 + r2, 2))
		print(f"PC = {hex(counter)} (\n  Binary = {printed}\n  Hexadecimal = {hexPrinted}\n);\n")
		
	elif type == "Data":
		if registers.get(r1) == None:
			print(f"Register in line {counter} it's wrong: {r1}")
			return

		elif registers.get(r2) == None:
			print(f"Register in line {counter} it's wrong: {r2}")
			return

	
	elif type == "Operation-Data":
		if registers.get(r1) == None:
			print(f"Register in line {counter} it's wrong: {r1}")
			return

		r1 = registers.get(r1)
		opcode = bin(opcode).replace('0b', '')
		opcode = opcode.zfill(4)

		r1 = bin(r1).replace('0b', '')
		r1 = r1.zfill(2)

		imm = bin(int (imm)).replace('0b', '')
		imm = imm.zfill(2)

		printed = (opcode + " " + r1 + imm)
		hexPrinted = hex(int(opcode + r1 + imm, 2))
		print(f"PC = {hex(counter)} (\n  Binary = {printed}\n  Hexadecimal = {hexPrinted}\n);\n")

	
	elif type == -1:
		print(f"PC = {hex(counter)} (\n  Binary = 0000 0000\n  Hexadecimal = 0x00\n);\n")

	os.system("pause")
	os.system("cls")

def compile(type, r1, r2, imm, counter, opcode, fileCompile):
	if type == "Operation":
		if registers.get(r1) == None:
			print(f"Register in line {counter} it's wrong: {r1}")
			exit(0)

		elif registers.get(r2) == None:
			print(f"Register in line {counter} it's wrong: {r2}")
			exit(0)

		r1 = registers.get(r1)
		r2 = registers.get(r2)

		# print
		opcode = bin(opcode).replace('0b', '')
		opcode = opcode.zfill(4)

		r1 = bin(r1).replace('0b', '')
		r1 = r1.zfill(2)
		r2 = bin(r2).replace('0b', '')
		r2 = r2.zfill(2)
		counter = bin(counter).replace('0b', '')
		counter = counter.zfill(8)
		printed = (opcode + " " + r1 + r2)
		
		
		fileCompile.write(f"{counter} {printed}\n")
		
	elif type == "Data":
		if registers.get(r1) == None:
			print(f"Register in line {counter} it's wrong: {r1}")
			exit(0)

		elif registers.get(r2) == None:
			print(f"Register in line {counter} it's wrong: {r2}")
			exit(0)

	
	elif type == "Operation-Data":
		if registers.get(r1) == None:
			print(f"Register in line {counter} it's wrong: {r1}")
			exit(0)

		r1 = registers.get(r1)
		opcode = bin(opcode).replace('0b', '')
		opcode = opcode.zfill(4)

		r1 = bin(r1).replace('0b', '')
		r1 = r1.zfill(2)

		imm = bin(int (imm)).replace('0b', '')
		imm = imm.zfill(2)
		counter = bin(counter).replace('0b', '')
		counter = counter.zfill(8)

		printed = (opcode + " " + r1 + imm)
		fileCompile.write(f"{counter} {printed}\n")

	
	elif type == -1:
		counter = bin(counter).replace('0b', '')
		counter = counter.zfill(8)
		fileCompile.write(f"{counter} 0000 0000\n")


def __main__():
	os.system("cls")
	option = int(input("\t\tCOMPILER\nEnter mode\n1. Show code in binary/hexadecimal \n2. Compile\nOption: "))
	# Enter file name
	os.system("cls")
	file = input("Enter name's file: ")
	os.system("cls")
	try:
		asmcode = open(file, "r")
		
	# Error
	except:
		print("No file found");
		os.system("pause")
		os.system("cls")
		__main__()
	if option == 1:
		i = 0
		#code iterator
		while (True):
			# catch instruction
			linea = asmcode.readline()
			linea = linea.upper()
			linea = linea.split()

			if not(str(linea).find(":") == -1):
				continue
		
			i += 1;
			
			if not linea:
				break
			
			opcode = opcodes.get(linea[0])
			print("\t\tINSTRUCTION\n")
			print(f"{i}: {linea}")
			
			typeInst = -1
			reg1 = ""
			reg2 = ""
			imm = ""


			if opcode == 0:
				# binaryInst = "0x00"
				typeInst = -1
				reg1 = "A"
				reg2 = "A"

			elif (opcode >= 1 and opcode <= 4) or (opcode >= 8 and opcode <= 9) or opcode == 11:
				typeInst = "Operation"
				reg1 = linea[1].replace(',', '')
				reg2 = linea[2].replace(',', '')

			elif opcode == 10:
				typeInst = "Operation-Data"
				reg1 = linea[1].replace(',', '')
				imm = linea[2]
				
				if int(imm) > 3:
					print(f"Syntax error in line: {i} const number is greater that 3, you put: {imm}")
					exit(0)
				

			elif opcode == None:
				print(f"Syntax error in line: {i} you put: {linea[0]}")
				exit(0)

			transform(typeInst, reg1, reg2, imm, i, opcode)	
		os.system("pause")
		os.system("cls")
	
	elif option == 2:
		os.system("cls")
		comp = open(file.replace(".s", ".txt"), 'w')
		i = 0
		#code iterator
		while (True):
			# catch instruction
			linea = asmcode.readline()
			linea = linea.upper()
			linea = linea.split()

			if not(str(linea).find(":") == -1):
				continue
			
			i += 1;
			
			if not linea:
				break
			
			opcode = opcodes.get(linea[0])
			typeInst = -1
			reg1 = ""
			reg2 = ""
			imm = ""


			if opcode == 0:
				# binaryInst = "0x00"
				typeInst = -1
				reg1 = "A"
				reg2 = "A"

			elif (opcode >= 1 and opcode <= 4) or (opcode >= 8 and opcode <= 9) or opcode == 11:
				typeInst = "Operation"
				reg1 = linea[1].replace(',', '')
				reg2 = linea[2].replace(',', '')

			elif opcode == 10:
				typeInst = "Operation-Data"
				reg1 = linea[1].replace(',', '')
				imm = linea[2]
				
				if int(imm) > 3:
					print(f"Syntax error in line: {i} const number is greater that 3, you put: {imm}")
					exit(0)
				

			elif opcode == None:
				print(f"Syntax error in line: {i} you put: {linea[0]}")
				exit(0)

			compile(typeInst, reg1, reg2, imm, i, opcode, comp)	
		print("Compiled successfully completed!")
		os.system("pause")
		os.system("cls")
	
	else:
		print("Enter valid option")
		os.system("pause")
		os.system("cls")
		__main__()


__main__()