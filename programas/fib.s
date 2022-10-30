ADDC R1, R0, 10  
ADDC R3, R0, 1	 
JAL 0xc					 
EXIT						 
ADDC R5, R5, 1   
JEQ R5, R1, 0x21 
ADD R4, R2, R3   
ADDC R2, R3, 0   
ADDC R3, R4, 0   
ADDC R5, R5, 1   
JMP 0xf					 
RET							 