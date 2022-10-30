from src.dictionaries import *
from os import system

def compile(file, compiled_file):
	counter = 0
	while True:
		system("cls")
		linea = file.readline()
		if not linea:
			break
		counter += 3
		linea = str(linea).split()
		op = opcodes.get(linea[0])
		opcode = bin(op).replace('0b', '').zfill(4)
		if op == 0:
			rd = bin(regs.get(linea[1].replace(',', ''))).replace('0b', '').zfill(5)
			r1 = bin(regs.get(linea[2].replace(',', ''))).replace('0b', '').zfill(5)
			r2 = bin(regs.get(linea[3].replace(',', ''))).replace('0b', '').zfill(5)
			funct = bin(functs.get(linea[0])).replace('0b', '').zfill(5)
			inst_hex = hex(int(opcode + r1 + r2 + rd + funct, 2)).replace('0x', '').zfill(6)

			compiled_file.write(f"[{hex(counter)}] 0x" + inst_hex + " # " + str(linea) + "\n")
		elif op == 3 or op == 11:
			compiled_file.write(f"[{hex(counter)}] {hex(int(opcode, 2))}00000" + " # " + str(linea) + "\n")
		elif op >= 6 and op <= 9:
			r1 = bin(regs.get(linea[1].replace(',', ''))).replace('0b', '').zfill(5)
			r2 = bin(regs.get(linea[2].replace(',', ''))).replace('0b', '').zfill(5)
			address = bin(int(linea[3].replace(',', ''), 16)).replace('0b', '').zfill(10)

			inst_hex = hex(int(opcode + r1 + r2 + address, 2)).replace('0x', '').zfill(6)
			compiled_file.write(f"[{hex(counter)}] 0x" + inst_hex + " # " + str(linea) + "\n")

		elif op == 4:
			rd = bin(regs.get(linea[1].replace(',', ''))).replace('0b', '').zfill(5)
			r1 = bin(regs.get(linea[2].replace(',', ''))).replace('0b', '').zfill(5)
			const = bin(int(linea[3].replace(',', ''), 10)).replace('0b', '').zfill(10)

			inst_hex = hex(int(opcode + r1 + rd + const, 2)).replace('0x', '').zfill(6)
			compiled_file.write(f"[{hex(counter)}] 0x" + inst_hex + " # " + str(linea) + "\n")
		elif op == 5 or op == 10:
			address = bin(int(linea[1].replace(',', ''), 16)).replace('0b', '').zfill(10)
			inst_hex = hex(int(address, 2)).replace('0x', '').zfill(6)
			compiled_file.write(f"[{hex(counter)}] 0x" + inst_hex + " # " + str(linea) + "\n")
	print("Compile successfully!")
	system("pause")
	system("cls")

def main():
	name = input("Ingrese archivo: ")
	try:
		file = open(name, 'r')
	except:
		print("Error, archivo no existente!")
		exit(0)

	compiled_file = open(name.replace(".asm", '').replace(".s", '') + ".bin", 'w')
	compile(file, compiled_file)

	file.close()
if __name__ == '__main__':
	main()