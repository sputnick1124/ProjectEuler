#include <stdio.h>
#include <stdlib.h>
#include <gmp.h>
#include <time.h>

clock_t start, end;
double time_tot;

int main(int argc, char *argv[])
{
	start = clock();
	mpz_t i, a, b, n, sum, mod;
	mpz_inits(a, b, i, n, sum, mod, NULL);
	mpz_set_ui(a, 1);
	mpz_set_ui(b, 1);
	mpz_set_str(n, argv[1], 10);
	while(mpz_cmp(i,n)<0) {
		mpz_add(i,a,b);
		mpz_mod_ui(mod,i,2);
		if(mpz_cmp_ui(mod, 0)==0) {
			mpz_add(sum,sum,i);
		}
		mpz_set(a,b);
		mpz_set(b,i);
	}
	mpz_out_str(stdout, 10, sum);
	printf("\n");
	mpz_clears(i, a, b, n, sum, NULL);
	end = clock();
	time_tot = (double) (end-start) / CLOCKS_PER_SEC;
	printf("%f seconds\n",time_tot);
	return 0;
}
