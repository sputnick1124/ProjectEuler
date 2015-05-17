#include <stdio.h>
#include <gmp.h>

int main(int argc, char *argv[])
{
	mpz_t n;
	mpz_init(n);
	mpz_set_ui(n,0);
	mpz_set_str(n, argv[1], 10);
	mpz_out_str(stdout,10,n);
	printf("\n");
	mpz_clear(n);
	return 0;
}
