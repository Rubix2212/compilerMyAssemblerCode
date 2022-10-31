@main:
ADDC R1, R0, 5
ADDC R3, R0, 1
ADDC R2, R0, 1
ADDC R1, R1, 1
JAL loop
EXIT
@loop:
JEQ R2, R1, return
MUL R3, R3, R2
ADDC R2, R2, 1
JMP loop
@return:
RET