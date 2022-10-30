#include <stdio.h>

int r2 = 0, r3 = 1, r4, r5, r1;

int fib(int r1) {
	for (r5 = 1; r5 != r1; r5++) {
		r4 = r2 + r3;
		r2 = r3;
		r3 = r4;
	}

	return r4;
}

int main() {
	printf("Ingrese numero: ");
	scanf("%d", &r1);
	
	printf("Fib: %d", fib(r1));
}