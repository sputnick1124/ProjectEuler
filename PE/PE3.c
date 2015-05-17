#include <stdio.h>
#include <stdlib.h>
#include <gmp.h>

int main(int argc, char *argv[]){
	mpz_t x, num, mod;
	mpz_inits(x, num, mod, NULL);
	mpz_set_str(num, argv[1], 10);
	mpz_set_ui(x, 2);
	while(mpz_cmp_ui(num, 1) != 0) {
		mpz_mod(mod, num, x);
		if(mpz_cmp_ui(mod, 0) == 0) {
			mpz_cdiv_q(num,num,x);
		}
		else {
			mpz_add_ui(x, x, 1);
		}
	}
	mpz_out_str(stdout, 10, x);
	printf("\n");
	return 0;
}
