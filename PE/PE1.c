#include <stdio.h>
#include <stdlib.h>

int main(int argc, char *argv[])
{
	long long sum = 0;
	int i;
	int n;
	n = atoi(argv[1]);

	for(i=0; i<n; ++i)
	{
		if (!(i%3) || !(i%5))
		{
			sum += (long) i;
		}
	}
	printf("%lld\n",sum);
	return 0;
}

