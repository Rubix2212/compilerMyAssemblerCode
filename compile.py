from io import TextIOWrapper
from sys import argv
from turtle import st
import numpy as np
from src.dictionaries import *
from os import system
	

def handleAddress(pc_at: list, pc_tag: list, to_search: str):
	try:
		index = pc_tag.index(to_search)
	except:
		print(f"La etiqueta {to_search} no existe")
		system("pause")
		exit(0)

	return pc_at.__getitem__(index)

def compile(file: TextIOWrapper, compiled_file: TextIOWrapper):
	counter = 0
	i = 0
	pc_at = []
	pc_tag = []
	file2 = file
	while True:
		linea2 = file2.readline()
		if not linea2:
			break
		if linea2[0][0] == "@":
			pc = hex(counter).replace('0x','').zfill(3)
			tag = linea2.replace('@', '').replace(':', '').replace('\n', '')
			pc_at.append(pc)
			pc_tag.append(tag)
			i += 1
			continue
	
		counter += 3		
	counter = 0
	jj = 1
	file = open(argv[1], "r")
	while jj:
		linea = file.readline()
		if not linea:
			break
		if linea[0][0] == "@":
			PC = hex(counter).replace('0x','').zfill(3)
			compiled_file.write(f"[0x{PC}] {linea}")
			continue

		
		linea = str(linea).split()
		op = opcodes.get(linea[0])
		opcode = bin(op).replace('0b', '').zfill(4)
		if op == 0:
			rd = bin(regs.get(linea[1].replace(',', ''))).replace('0b', '').zfill(5)
			r1 = bin(regs.get(linea[2].replace(',', ''))).replace('0b', '').zfill(5)
			r2 = bin(regs.get(linea[3].replace(',', ''))).replace('0b', '').zfill(5)
			funct = bin(functs.get(linea[0])).replace('0b', '').zfill(5)
			inst_hex = hex(int(opcode + r1 + r2 + rd + funct, 2)).replace('0x', '').zfill(6)

			PC = hex(counter).replace('0x','').zfill(3)
			compiled_file.write(f"[0x{PC}] 0x" + inst_hex + "    			# " + str(linea) + "\n")
		elif op == 3 or op == 11:
			PC = hex(counter).replace('0x','').zfill(3)
			compiled_file.write(f"[0x{PC}] {hex(int(opcode, 2))}00000" + "    			# " + str(linea) + "\n")
		elif op >= 6 and op <= 9:
			r1 = bin(regs.get(linea[1].replace(',', ''))).replace('0b', '').zfill(5)
			r2 = bin(regs.get(linea[2].replace(',', ''))).replace('0b', '').zfill(5)
			address = handleAddress(pc_at, pc_tag, linea[3].replace(',', '').lower())
			address = bin(int(address, 16)).replace('0b', '').zfill(10)

			inst_hex = hex(int(opcode + r1 + r2 + address, 2)).replace('0x', '').zfill(6)
			PC = hex(counter).replace('0x','').zfill(3)
			compiled_file.write(f"[0x{PC}] 0x" + inst_hex + "    			# " + str(linea) + "\n")

		elif op == 4:
			rd = bin(regs.get(linea[1].replace(',', ''))).replace('0b', '').zfill(5)
			r1 = bin(regs.get(linea[2].replace(',', ''))).replace('0b', '').zfill(5)
			const = bin(int(linea[3].replace(',', ''), 10)).replace('0b', '').zfill(10)

			inst_hex = hex(int(opcode + r1 + rd + const, 2)).replace('0x', '').zfill(6)
			PC = hex(counter).replace('0x','').zfill(3)
			compiled_file.write(f"[0x{PC}] 0x" + inst_hex + "    			# " + str(linea) + "\n")
		elif op == 5 or op == 10:
			address = handleAddress(pc_at, pc_tag, linea[1].replace(',', '').lower())
			address = bin(int(address, 16)).replace('0b', '').zfill(10)
			inst_hex = hex(int(opcode + "0000000000" + address, 2)).replace('0x', '')
			compiled_file.write(f"[0x{PC}] 0x" + inst_hex + "    			# " + str(linea) + "\n")
		
		counter += 3 
	print("Compile successfully!")

def main():
	try:
		file = open(argv[1], 'r')
	except:
		print("Error, archivo no existente!")
		exit(0)

	compiled_file = open(argv[1].replace(".asm", '').replace(".s", '') + ".bin", 'w')
	compile(file, compiled_file)

	file.close()
if __name__ == '__main__':
	main()