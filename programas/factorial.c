#include <stdio.h>

int main() {
	int r1, r2, r3, r4, r5, r6, r7;
	printf("Ingrese numero: ");
	scanf("%d", &r1);
	r3 = 1;
	for (r2 = 1; r2 != r1 + 1; r2++) {
		r3 = r3 * r2;
	}
	printf("Factorial: %d", r3);
}