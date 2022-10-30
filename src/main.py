from audioop import add
from tabulate import tabulate
from dictionaries import *
from os import system

def main():
	while True:
		system("cls")
		inst = []
		inp = input("Ingrese instruccion: ").upper()
		if inp == "0":
			break
		ininst = inp
		inp = inp.split()
		op = opcodes.get(inp[0])
		opcode = bin(op).replace('0b', '').zfill(4)
		if op == 0:
			rd = bin(regs.get(inp[1].replace(',', ''))).replace('0b', '').zfill(5)
			r1 = bin(regs.get(inp[2].replace(',', ''))).replace('0b', '').zfill(5)
			r2 = bin(regs.get(inp[3].replace(',', ''))).replace('0b', '').zfill(5)
			funct = bin(functs.get(inp[0])).replace('0b', '').zfill(5)
			inst_hex = hex(int(opcode + r1 + r2 + rd + funct, 2)).replace('0x', '').zfill(6)

			inst = [["Instruction", ininst],
							["opcode", opcode],
							["r1", r1],
							["r2", r2],
							["rd", rd],
							["funct", funct],
							["Inst in hex", "0x" + inst_hex]]
		elif op == 3 or op == 11:
			inst = [["Instruction", ininst],
							["opcode", opcode],
							["Inst in hex", f"0x{hex(int(opcode, 2))}00000"]]
		elif op >= 6 and op <= 9:
			r1 = bin(regs.get(inp[1].replace(',', ''))).replace('0b', '').zfill(5)
			r2 = bin(regs.get(inp[2].replace(',', ''))).replace('0b', '').zfill(5)
			address = bin(int(inp[3].replace(',', ''), 16)).replace('0b', '').zfill(10)

			inst_hex = hex(int(opcode + r1 + r2 + address, 2)).replace('0x', '').zfill(6)
			inst = [["Instruction", ininst],
							["opcode", opcode],
							["r1", r1],
							["r2", r2],
							["address", address],
							["Inst in hex", "0x" + inst_hex]]

		elif op == 4:
			rd = bin(regs.get(inp[1].replace(',', ''))).replace('0b', '').zfill(5)
			r1 = bin(regs.get(inp[2].replace(',', ''))).replace('0b', '').zfill(5)
			const = bin(int(inp[3].replace(',', ''), 10)).replace('0b', '').zfill(10)

			inst_hex = hex(int(opcode + r1 + rd + const, 2)).replace('0x', '').zfill(6)
			inst = [["Instruction", ininst],
							["opcode", opcode],
							["r1", r1],
							["rd", rd],
							["const", const],
							["Inst in hex", "0x" + inst_hex]]
		elif op == 5 or opcode == 10:
			
			address = bin(int(inp[1].replace(',', ''), 16)).replace('0b', '').zfill(10)
			inst_hex = hex(int(address, 2)).replace('0x', '').zfill(6)
			inst = [["Instruction", ininst],
							["opcode", opcode],
							["r1", "00000"],
							["rd", "00000"],
							["address", address],
							["Inst in hex", "0x" + inst_hex]]
		print(tabulate(inst, tablefmt="grid"))
		system("pause")
	system("cls")

if __name__ == '__main__':
	main()