ADDC R6, R0, 10 
ADDC R1, R0, 0
ADDC R2, R0, 1
ADDC R4, R4, 1
JEQ R4, R3, 24
ADD R1, R1, R2
ADD R2, ZERO, R1
ADD R2, R1, R2
ADDC R4, R4, 1
JEQ R4, R3, 24
ADD R5, ZERO, R2
JMP 6
