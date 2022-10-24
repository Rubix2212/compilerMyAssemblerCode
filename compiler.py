from os import system

opcodes = {
	"ADD": 0,
	"SUB": 0,
	"MUL": 0,
	"DIV": 0,
	"AND": 0,
	"OR": 0,
	"XOR": 0,
	"NAND": 0,
	"LD": 1,
	"SD": 2,
	"RET": 3,
	"ADDC": 4,
	"JMP": 5,
	"JEQ": 6,
	"JNE": 7,
	"JLT": 8,
	"JGT": 9,
	"JAL": 10,
	"SYSCALL": 11
}

registros = {
	"ZERO": 0,
	"R0": 0,
	"R1": 1,
	"R2": 2,
	"R3": 3,
	"R4": 4,
	"R5": 5,
	"R6": 6,
	"R7": 7
}

functs = {
	"ADD": 0,
	"SUB": 1,
	"MUL": 2,
	"DIV": 3,
	"AND": 4,
	"OR": 5,
	"XOR": 6,
	"NAND": 7
}

def printcode(linea, counter, compiled):
	
	opcode = opcodes.get(linea[0])
	if opcode == 0:
		opcode = str(bin(opcode)).replace("0b", '').zfill(4)
		rd = str(linea[1]).replace(",", '')
		r1 = str(linea[2]).replace(",", '')
		r2 = str(linea[3]).replace(",", '')
		rd = str(bin(registros.get(rd))).replace("0b", '').zfill(3)
		r1 = str(bin(registros.get(r1))).replace("0b", '').zfill(3)
		r2 = str(bin(registros.get(r2))).replace("0b", '').zfill(3)
		funct = str(bin(functs.get(linea[0]))).replace("0b", '').zfill(3)
		counter = hex(counter).replace("0x", '').zfill(2)
		hexinst = str(hex(int(opcode + r1 + r2 + rd + funct, 2))).replace("0x", '').zfill(4)
		linea = str(linea).replace("[", '').replace("]", '').replace(",", '').replace("'", '')
		compiled.write(f"[0x{counter}] {opcode}{r1}{r2}{rd}{funct} => 0x{hexinst} # {str(linea)}\n")

	elif opcode == 5 or opcode == 10:
		opcode = str(bin(opcode)).replace("0b", '').zfill(4)
		address = str(bin(int(linea[1]))).replace("0b", '').zfill(12)
		hexinst = str(hex(int(opcode + address, 2))).replace("0x", '').zfill(4)
		counter = hex(counter).replace("0x", '').zfill(2)
		linea = str(linea).replace("[", '').replace("]", '').replace(",", '').replace("'", '')	
		compiled.write(f"[0x{counter}] {opcode}{address} => 0x{hexinst} # {str(linea)}\n")
	
	elif opcode == 3 or opcode == 11:
		opcode = str(bin(opcode)).replace("0b", '').zfill(4)
		rem = "000000000000"
		hexinst = str(hex(int(opcode + rem, 2))).replace("0x", '').zfill(4)
		counter = hex(counter).replace("0x", '').zfill(2)
		linea = str(linea).replace("[", '').replace("]", '').replace(",", '').replace("'", '')	
		compiled.write(f"[0x{counter}] {opcode}{rem} => 0x{hexinst} # {str(linea)}\n")

	elif opcode == 4 or opcode >= 6 or opcode <= 9:
		opcode = str(bin(opcode)).replace("0b", '').zfill(4)
		rd = str(linea[1]).replace(",", '')
		r1 = str(linea[2]).replace(",", '')
		imm = str(linea[3]).replace(",", '')
		rd = str(bin(registros.get(rd))).replace("0b", '').zfill(3)
		r1 = str(bin(registros.get(r1))).replace("0b", '').zfill(3)
		imm = str(bin(int(imm))).replace("0b", '').zfill(6)
		counter = hex(counter).replace("0x", '').zfill(2)
		hexinst = str(hex(int(opcode + r1 + rd + imm, 2))).replace("0x", '').zfill(4)
		linea = str(linea).replace("[", '').replace("]", '').replace(",", '').replace("'", '')
		compiled.write(f"[0x{counter}] {opcode}{r1}{rd}{imm} => 0x{hexinst} # {str(linea)}\n")

def compile(code):
	counter = 0
	compiled = open(f"compiled.s", "w")
	while True:
		linea = code.readline().split()
		if not linea:
			break
		
		linea = linea
		printcode(linea, counter, compiled)
		counter += 2

	compiled.close()

def __main__():
	system("color F")
	system("cls")
	nombre = input("Ingrese nombre del archivo: ")
	
	try:
		code = open(nombre, "r")
	except:
		system("cls")
		system("color 4")
		print("Error! Ingrese nombre / direccion del archivo")
		system("pause")
		system("cls")
		__main__()

	compile(code)

	code.close()

__main__()