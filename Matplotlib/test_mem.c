#include <stdio.h>
#include <stdlib.h>

int main()
{
	int i=0;
	for(i=0; i<30000; ++i){
		malloc(1024);
		printf("allocate mem succ!\n");
	}
	return 0;
}