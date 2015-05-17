#include <stdio.h>
#include <stdlib.h>

int main(int argc, char *argv[])
{
	unsigned long long i = 0;
	unsigned long long a = 1;
	unsigned long long b = 1;
	unsigned long long sum = 0;
	unsigned long long n;
	n = atoi(argv[1]);
	while(i < n) {
		i = a + b;
		if(i%2 == 0) {
			sum += i;
		}
		a = b;
		b = i;
	}
	printf("%lld\n",sum);
	return 0;
}
